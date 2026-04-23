class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv","9": "wxyz"}
        out =  [""]
        
        for d in digits:
            out1 = []
            for i in out:
                for j in mapping[d]:
                    out1.append(i + j)
            out = out1

        return out
    
a = Solution()
print(a.letterCombinations("3425"))