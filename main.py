default_server = {'clients': [], 'time_live': 0, 'is_active': True}
servers = [
        default_server
]

def get_active_servers(servers):
    """Count the active servers.

    Keyword arguments:
    servers -- list of all servers
    """
    result = 0
    for server in servers:
        if server['is_active']:
            result += 1
    return result

def is_full(servers, umax):
    """Return if servers is full

    Keyword arguments:
    servers -- list of all servers
    umax -- max capacity of users in server
    """
    result = 0
    for server in servers:
        if len(server['clients']) == umax:
            result += 1

    if result == len(servers):
        return True
    else:
        return False

def add_server(servers):
    """Add a new server to a list of servers

    Keyword arguments:
    servers -- list of all servers
    """
    default_server = {'clients': [], 'time_live': 0, 'is_active': True}
    servers.append(default_server)

def add_clients(clients, servers, umax, ttask):
    """Add new clients to servers

    Keyword arguments:
    clients -- number of new clients in the server
    servers -- list of all servers
    umax --  max capacity of users in server
    ttask -- max tasks that user can exec into the server
    """
    client = {'ttask':0, 'is_active':True}
    for i in range(clients, 0, -1):
        if is_full(servers, umax):
            add_server(servers)
        if not is_full(servers, umax):
            for server in servers:
                if server['is_active']:
                    if len(server['clients']) < umax:
                        server['clients'].append(client)
                    update_ttasks(server, ttask, umax)

def update_ttasks(server, ttask, umax):
    """Update user tasks in the server

    Keyword arguments:
    server -- server that execute the update
    ttask -- max tasks that user can exec into the server
    umax --  max capacity of users in server
    """
    if server['is_active']:
        server['time_live'] += 1

        for i in range(0, len(server['clients'])):
            if server['clients'][i]['ttask'] < ttask:
                server['clients'][i]['ttask'] += 1
            else:
                server['clients'][i]['is_active'] = False

        count = 0
        actives = 0
        for i in range(0, len(server['clients'])):
            if not server['clients'][i]['is_active']:
                count += 1
        if count == umax:
            deactivate_server(server)

def deactivate_server(server):
    """Deactivate server

    Keyword arguments:
    server -- server that will be deactivated
    """
    server['is_active'] = False

def load_balance(input_server):
    list_input = input_server.split(" ")
    ttask = int(list_input.pop(0))
    umax = int(list_input.pop(0))
    input_clients = [int(s) for s in list_input]
    result = ""
    for clients in input_clients:
        add_clients(clients, servers, umax, ttask)
        for server in servers:
            result += str(len(server['clients'])) + ","
        result += "\n"

    while get_active_servers(servers) >= 1:
        for server in servers:
            if server['is_active']:
                update_ttasks(server, ttask, umax)
            result += str(len(server['clients'])) + ","
        result += "\n"
    total_ticks = 0
    for server in servers:
        total_ticks += server['time_live']

    result += str(total_ticks)
    return result

load_balance("4 2 1 3 0 1 0 1")
