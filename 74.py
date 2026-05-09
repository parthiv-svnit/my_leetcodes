class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchr(target, l, r) :
            if l > r :
                return r
            m = (l + r) // 2
            if matrix[m][0] < target :
                return searchr(target, m + 1, r)
            elif matrix[m][0] > target :            
                return searchr(target, l, m - 1)
            else :
                return m
        
        r = searchr(target, 0, len(matrix) - 1)

        if target in matrix[r] :
            return True
        else :
            return False