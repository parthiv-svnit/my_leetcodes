class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        x = 5
        temp = n // x
        while temp > 0 :
            out += temp
            x *= 5
            temp = n // x
        return out