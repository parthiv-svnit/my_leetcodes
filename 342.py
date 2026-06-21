class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        while n > 4 :
            if n % 4 != 0 :
                return False
            n //= 4
        if n < 4 and n != 1 :
            return False
        return True
        