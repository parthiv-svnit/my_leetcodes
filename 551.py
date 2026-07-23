class Solution:
    def checkRecord(self, s: str) -> bool:
        di = Counter(s)
        print(di)
        if di['A'] >= 2 :
            return False
        n = len(s)
        for i in range(n) :
            if s[i] == 'L' :
                count = 1
                i += 1
                while i < n and s[i] == 'L' :
                    count += 1
                    i += 1
                    if count == 3 :
                        return False
        return True