class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c :
            return mat
        mi, ni = 0, 0
        i = 0
        out = [[0] * c for _ in range(r)]
        while i < r :
            j = 0
            while j < c :
                if ni == n :
                    if mi == m - 1 :
                        return out
                    ni = 0
                    mi += 1
                
                out[i][j] = mat[mi][ni]
                ni += 1

                j += 1
            i += 1
        return out