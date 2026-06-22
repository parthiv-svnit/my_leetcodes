class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 1
        dp = [1] * (n + 1) 
        dp[1] = 9
        x = 9
        i = 2
        while i <= n :
            dp[i] = dp[i - 1] * x
            i += 1
            x -= 1
        return sum(dp)