class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2 :
            return n
        
        f = 1
        s = 2

        for i in range(3, n + 1) :
            f, s = s, f + s

        return s