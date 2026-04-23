class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        def backtrack(string,i,j):
            if len(string) == 2*n :
                out.append(string)
                return
            
            if i < n :
                backtrack(string + "(", i + 1, j)
            
            if j < i :
                backtrack(string + ")", i, j + 1)
        
        backtrack("",0,0)

        return out
             