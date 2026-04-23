class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        i = 0
        while i < min((len(strs[0])),(len(strs[1]))) :
            if (strs[0])[i] != (strs[1])[i] :
                break
            i+=1
            
        
        def fun(j,i):
            k = 0
            if j >= len(strs):
                return strs[0][:i]
            
            while k < i and k < len(strs[j]):
                if (strs[j])[k] != (strs[0])[k] :
                    
                    return fun(j+1,k)
                
                k += 1  
            return fun(j+1,k)   
        return fun(2,i)

a = Solution()
print(a.longestCommonPrefix(["flower", "flow", "flour"]))