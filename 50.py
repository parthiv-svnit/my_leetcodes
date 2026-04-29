class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        out = 1.0

        while n > 0:
            if n & 1:
                out *= x
            
            x *= x
            n >>= 1
        return out