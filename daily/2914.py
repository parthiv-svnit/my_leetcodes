class Solution:
    def minChanges(self, s: str) -> int:
        out = 0
        n = len(s)
        for i in range(0, n, 2) :
            if i > n - 1 :
                break
            if s[i + 1] != s[i] :
                out += 1
        return out