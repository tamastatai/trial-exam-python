import unittest
from exc4 import greeter

class Test_exc4(unittest.Testcase):
    #AttributeError: module 'unittest' has no attribute 'Testcase' -- ?? :(

    def test_empty(self):
        self.assertEqual(greeter(""), 'Hello, Mr Nobody!')

    def test_num(self):
        self.assertEqual(greeter(9), 'Hello, 9!')

    def test_char(self):
        self.assertEqual(greeter("X"), 'Hello, X!')

    def test_list(self):
        self.assertEqual(greeter(["one","two","three"]), 'Hello, Mr Nobody!')

if __name__ == '__main__':
    unittest.main()
