class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        out = 0
        for i in columnTitle :
            out = (out * 26) + (ord(i) - 64)
        return out