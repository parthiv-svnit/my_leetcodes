class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        out = 1
        r = 0
        l = 0
        n = len(s)
        di = defaultdict(int)
        di[s[0]] = 1
        out = 1
        while r < n :
            if r != n - 1 :
                di[s[r + 1]] += 1
                while di[s[r + 1]] > 2 :
                    di[s[l]] -= 1
                    l += 1
                out = max(out, r - l + 2)
            r += 1
        return out