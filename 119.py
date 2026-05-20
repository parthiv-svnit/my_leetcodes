class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        fr = [1]
        if rowIndex == 0 :
            return fr

        j = 0
        while j < rowIndex :
            i = 0
            sr = []
            sr.append(1)
            while i < len(fr) - 1 :
                sr.append(fr[i] + fr[i + 1])
                i += 1
            sr.append(1)
            fr = sr
            j += 1
        return fr