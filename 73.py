class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        remr = set()
        remc = set()
        # for row in range(len(matrix)) :
        #     remc.add(i for i, val in enumerate(matrix[row]) if val == 0)
        #     if 0 in matrix[row] :
        #         remr.add(row)
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    remr.add(i)
                    remc.add(j)

        for i in remc :
            for j in range(len(matrix)) :
                matrix[j][i] = 0
        for j in remr :
            matrix[j] = [0] * (len(matrix[0]))