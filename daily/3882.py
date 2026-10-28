class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        i = 0
        while i < m :
            j = 0
            while j < n :
                if not i and not j :
                    j += 1
                    continue
                if i :
                    for x in dp[i - 1][j] :
                        dp[i][j].add(x ^ grid[i][j])
                if j :
                    for x in dp[i][j - 1] : 
                        dp[i][j].add(x ^ grid[i][j])
                j += 1
            i += 1
        print(dp)
        return min(dp[-1][-1])