class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        out = 0
        for i in s :
            if i == '(' :
                l += 1
            else :
                if l > 0 :
                    l -= 1
                else :
                    out += 1
        return l + out