class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1 :
            return s
        di = Counter(s)
        di = dict(sorted(di.items(), key = lambda x : x[0]))
        out = []
        midch = 0
        for i, j in di.items() :
            if j & 1 :
                midch = i
            di[i] //= 2
        for i, j in di.items() :
            while j :
                if di[i] :
                    out.append(i)
                j -= 1
        l = len(out)
        if midch :
            out.append(midch)
        for i in range(l - 1, -1, -1) :
            out.append(out[i])
        return "".join(out)