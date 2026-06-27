class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return format(num & 0xffffffff, 'x')