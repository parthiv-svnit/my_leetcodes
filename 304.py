class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix :
            self.arr = None
            return
        m = len(matrix)
        n = len(matrix[0])
        self.arr = [r[:] for r in matrix]
        for i in range(1, n) :
            self.arr[0][i] += self.arr[0][i - 1]
        for i in range(1, m) :
            self.arr[i][0] += self.arr[i - 1][0]
        for i in range(1, m) :
            for j in range(1, n) :
                self.arr[i][j] += self.arr[i - 1][j] + self.arr[i][j - 1] - self.arr[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0 :
            return self.arr[row2][col2]
        if row1 == 0 and col1 > 0:
            return self.arr[row2][col2] - self.arr[row2][col1 - 1]
        if row1 > 0 and col1 == 0 :
            return self.arr[row2][col2] - self.arr[row1 - 1][col2]

        return self.arr[row2][col2] - self.arr[row1 - 1][col2] - self.arr[row2][col1 - 1] + self.arr[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)