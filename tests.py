import unittest
import main

class TestLoadBalanceFunctions(unittest.TestCase):

    def test_load_balance(self):
        self.assertEqual(main.load_balance("4 2 1 3 0 1 0 1"), "1\n2,2\n2,2\n2,2,1\n1,2,1\n2\n2\n1\n1\n0\n15")

if __name__ == '__main__':
    unittest.main()
