class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        l = len(s1)
        temp = []
        out = []
        s = -1
        if s1[0] != s2[0] :
            s = 0
        e = -1
        for i in range(l) :
            if s1[i] == s2[i] :
                if s != -1 and e != -1 and s <= e:
                    out.append([s1[s:e + 1], s2[s:e + 1]])
                    # print(i, s, e)
                s = i + 1
                e = i
            else :
                e += 1
        if s != -1 and e != -1 and s <= e :
            out.append([s1[s:e + 1], s2[s:e + 1]])
        return out