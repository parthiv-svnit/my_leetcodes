class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        k = 0
        while k <= n :
            out = i
            i += 1
            k = i * (i + 1) // 2
        return out