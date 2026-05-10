class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c, i) :
            if i == len(word) :
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i] :
                return False
            
            temp = board[r][c]
            board[r][c] = '.'

            out = (dfs(r + 1, c, i + 1)) or (dfs(r, c + 1, i + 1)) or (dfs(r - 1, c, i + 1)) or (dfs(r, c - 1, i + 1))

            board[r][c] = temp

            return out
        
        for i in range(m) :
            for j in range(n) :
                if board[i][j] == word[0] :
                    if dfs(i, j, 0) :
                        return True
        
        return False