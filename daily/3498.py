class Solution:
    def reverseDegree(self, s: str) -> int:
        out = 0
        for i in range(len(s)) :
            out += (26 - (ord(s[i]) - 97)) * (i + 1)
        return out