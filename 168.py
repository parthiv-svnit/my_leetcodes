class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        out = ""
        while columnNumber > 0 :
            columnNumber -= 1
            out += chr( 65 + (columnNumber % 26))
            columnNumber //= 26
        return out[::-1]