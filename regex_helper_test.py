import unittest
from regex_helper import *

class TestRegexHelper(unittest.TestCase):
    def setUp(self):
        self.classUnderTest = RegexHelper()

    def testTestMethod(self):
        self.assertEquals("testMethod",self.classUnderTest.testMethod())

if __name__ == '__main__':
    unittest.main()
