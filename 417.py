class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0] :
            return []
        m = len(heights)
        n = len(heights[0])
        p = set()
        a = set()
        def fun(r, c, visited, prevcell) :
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or (r, c) in visited or heights[r][c] < prevcell :
                return 
            visited.add((r, c)) 

            fun(r + 1, c, visited, heights[r][c])
            fun(r - 1, c, visited, heights[r][c])
            fun(r, c + 1, visited, heights[r][c])
            fun(r, c - 1, visited, heights[r][c])
        
        for r in range(m) :
            fun(r, 0, p, heights[r][0])
            fun(r, n - 1, a, heights[r][n - 1])
        for c in range(n) :
            fun(0, c, p, heights[0][c])
            fun(m - 1, c, a, heights[m - 1][c])
        
        out = p & a
        
        return list(out)