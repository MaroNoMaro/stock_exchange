import re

class RegexHelper:
    """Class to handle regex"""

    def testMethod(self):
        return "testMethod"

    def findDecimalNumber(self, input_string):
        return re.match('[0-9]*.[0-9]*',input_string)
        