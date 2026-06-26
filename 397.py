class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        while n > 1 :
            if n & 1 :
                if n == 3 :
                    n -= 1
                elif n & 2 :
                    n += 1
                else :
                    n -= 1
            else :
                n //= 2
            out += 1
        return out