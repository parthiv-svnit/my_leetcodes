class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out = []
        
        t, d = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while t <= d and l <= r :
            for i in range(l, r + 1):
                out.append(matrix[t][i])
            t += 1
            for i in range(t, d + 1):
                out.append(matrix[i][r])
            r -= 1
            if not (l <= r and t <= d):
                break
            for i in range(r, l - 1, -1):
                out.append(matrix[d][i])
            d -= 1
            for i in range(d, t - 1, -1):
                out.append(matrix[i][l])
            l += 1 
        return out