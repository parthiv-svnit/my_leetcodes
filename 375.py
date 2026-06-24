class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        for l in range(2, n + 1) :
            for i in range(1, n - l + 2) :
                j = i + l - 1
                mincost = float('inf')
                for k in range(i, j + 1) :
                    temp = k + max(dp[i][k - 1], dp[k + 1][j])
                    mincost = min(temp, mincost)
                dp[i][j] = mincost
        return dp[1][n]