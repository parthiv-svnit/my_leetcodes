class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1 :
            return False
        
        di0 = Counter(s1)
        di = Counter(s2[:l1])
        if di == di0 :
            return True
        for i in range(1, l2 - l1 + 1) :
            di[s2[i - 1]] -= 1
            di[s2[i + l1 - 1]] += 1
            if di == di0 :
                return True
        return False