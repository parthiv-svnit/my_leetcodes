class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        out = [[boxGrid[i][j] for i in range(m-1,-1,-1)] for j in range(n)]
        
        for i in range(m) :
            j = n - 1
            k = j
            while j >= 0 :
                if out[j][i] == '#' :
                        out[j][i], out[k][i] = out[k][i], out[j][i]
                        k -= 1
                elif out[j][i] == '*' :
                        k = j - 1
                j -= 1
        return out
                    

        