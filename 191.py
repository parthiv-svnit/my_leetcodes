class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        o = 0
        while n > 0 :
            if n & 1 :
                o += 1
            n >>= 1
        return o