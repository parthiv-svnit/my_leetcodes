class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        q = deque()
        for i in range(m) :
            for j in range(n) :
                if mat[i][j] == 0 :
                    dp[i][j] = 0
                    q.append((i, j))
        
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q :
            i, j = q.popleft()
            for dx, dy in di :
                x, y = dx + i, dy + j
                if 0 <= x < m and 0 <= y < n :
                    if dp[x][y] > dp[i][j] :
                        dp[x][y] = dp[i][j] + 1
                        q.append((x, y))
        return dp