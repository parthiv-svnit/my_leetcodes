class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        out = [0]

        def fun(l, r) :
            while l >= 0 and r < n and s[l] == s[r] :
                print(l, r, s[l])
                out[0] += 1
                l -= 1
                r += 1
        for i in range(n) :
            fun(i, i)
            fun(i, i + 1)
        return out[0]