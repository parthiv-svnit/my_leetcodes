class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        out = 0
        ans = ''
        temp = ''
        for r in range(len(s)) :
            if s[r] == '1' :
                out += 1
            while out > k :
                if s[l] == '1' :
                    out -= 1
                l += 1
            
            if out == k :
                while s[l] == '0' :
                    l += 1
                temp = s[l: r + 1]
                if not ans or len(ans) > len(temp) :
                    ans = temp
                elif len(temp) == len(ans) and temp < ans :
                    ans = temp
        return ans