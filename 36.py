class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        box = [[] for _ in range(9)]
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                k = (i/3)*3 + (j/3)
                if board[i][j] == '.':
                    continue
                if board[i][j] not in (box[k] + row[i] + col[j]) :
                    box[k].append(board[i][j])
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                else:
                    return False
        
        return True