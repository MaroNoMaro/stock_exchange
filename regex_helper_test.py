import unittest
from regex_helper import *

class TestRegexHelper(unittest.TestCase):
    def setUp(self):
        self.classUnderTest = RegexHelper()

    def testTestMethod(self):
        self.assertEqual("testMethod",self.classUnderTest.testMethod())

    def test_number_Finder(self):
        self.assertEqual("0.92",self.classUnderTest.findDecimalNumber('<td class="textBold" id="referencePrice" data-value="0.92">0,92 zł</td>'))
        self.assertEqual("48.04",self.classUnderTest.findDecimalNumber('<td class="textBold" id="referencePrice" data-value="48.04">48,04 zł</td>'))
        # self.fail("not impremented")

if __name__ == '__main__':
    unittest.main()
