class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        i, j = 0, 0
        out = []
        turn = 1
        while i != m - 1 or j != n - 1 :
            if turn & 1 :
                while i > 0 and j < n - 1 :
                    out.append(mat[i][j])
                    i -= 1
                    j += 1
                
                out.append(mat[i][j])
                if j == n - 1 :
                    i += 1
                else :
                    j += 1

                turn = 2
            else  :
                while j > 0 and i < m - 1 :
                    out.append(mat[i][j])
                    i += 1
                    j -= 1
                
                out.append(mat[i][j])
                if i == m - 1 :
                    j += 1
                else :
                    i += 1

                turn = 1
        out.append(mat[m - 1][n - 1])
        return out