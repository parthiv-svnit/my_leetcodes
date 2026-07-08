class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = {}
        if m == 1 and n == 1 :
            return 4 if grid[0][0] else 0
        if m == 1 :
            if grid[0][0] :
                dp[(0, 0)] = 4 - (grid[0][1])
            if grid[0][n - 1] :
                dp[(0, n - 1)] = 4 - (grid[0][n - 2])    
            for i in range(1, n - 1) :
                if grid[0][i] :
                    dp[(0, i)] = 4 - (grid[0][i - 1] + grid[0][i + 1])
            return sum(dp.values())               
        if n == 1 :
            if grid[0][0] :
                dp[(0, 0)] = 4 - (grid[1][0])
            if grid[m - 1][0] :
                dp[(m - 1, 0)] = 4 - (grid[m - 2][0])    
            for i in range(1, m - 1) :
                if grid[i][0] :
                    dp[(i, 0)] = 4 - (grid[i - 1][0] + grid[i + 1][0])
            return sum(dp.values())               

        if grid[0][0] :
            dp[(0, 0)] = 4 - (grid[0][1] + grid[1][0])
        if grid[0][n - 1] :
            dp[(0, n - 1)] = 4 - (grid[0][n - 2] + grid[1][n - 1])        
        if grid[m - 1][0] :
            dp[(m - 1, 0)] = 4 - (grid[m - 2][0] + grid[m - 1][1])        
        if grid[m - 1][n - 1] :
            dp[(m - 1, n - 1)] = 4 - (grid[m - 1][n - 2] + grid[m - 2][n - 1])

        for i in range(1, n - 1) :
            if grid[0][i] :
                dp[(0, i)] = 4 - (grid[0][i - 1] + grid[0][i + 1] + grid[1][i])
        for i in range(1, m - 1) :
            if grid[i][0] :
                dp[(i, 0)] = 4 - (grid[i - 1][0] + grid[i][1] + grid[i + 1][0])
        for i in range(1, n - 1) :
            if grid[m - 1][i] :
                dp[(m - 1, i)] = 4 - (grid[m - 1][i - 1] + grid[m - 2][i] + grid[m - 1][i + 1])
        for i in range(1, m - 1) :
            if grid[i][n - 1] :
                dp[(i, n - 1)] = 4 - (grid[i - 1][n - 1] + grid[i][n - 2] + grid[i + 1][n - 1])

        for i in range(1, m - 1) :
            for j in range(1, n - 1) :
                if grid[i][j] :
                    dp[(i, j)] = 4 - (grid[i - 1][j] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j])
        return sum(dp.values())