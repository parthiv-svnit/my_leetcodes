class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = [[1]]
        
        ind = 1

        while ind < numRows :
            i = 0
            tarr = []
            tarr.append(1)
            while i < ind - 1 :
                tarr.append(arr[ind - 1][i] + arr[ind - 1][i + 1])
                i += 1
            arr.append(tarr)
            arr[-1].append(1)
            ind += 1
        return arr