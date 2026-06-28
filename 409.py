class Solution:
    def longestPalindrome(self, s: str) -> int:
        di = Counter(s)
        di = dict(sorted(di.items(), key = lambda x : x[1], reverse = True))
        print(di)
        count = 1
        out = 0
        for x, y in di.items() :
            if y & 1 and count == 1 :
                out += y
                count = 0
            elif y & 1 :
                out += y - 1
            elif not y & 1 :
                out += y
        return out