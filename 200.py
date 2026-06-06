class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        out = 0
        row = len(grid)
        col = len(grid[0])
        def fun(r, c) :
            if (not 0 <= r < row) or (not 0 <= c < col) or grid[r][c] == "0" :
                return
            grid[r][c] = "0"

            fun(r + 1, c)
            fun(r, c + 1)
            fun(r - 1, c)
            fun(r, c - 1)
        for r in range(row) :
            for c in range(col) :
                if grid[r][c] == "1" :
                    out += 1
                    fun(r, c)
        return out