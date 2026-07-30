class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        out = 0
        j = 0
        for i in word :
            if j > 23 :
                out += 4
            elif j > 15 :
                out += 3
            elif j > 7 :
                out += 2
            else :
                out += 1
            j += 1
        return out