class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = deque()
        d = deque()
        for i in range(n) :
            if senate[i] == 'R' :
                r.append(i)
            else :
                d.append(i)
        
        while r and d :
            r0 = r.popleft()
            d0 = d.popleft()
            if r0 < d0 :
                r.append(r0 + n)
            else :
                d.append(d0 + n)
        return "Radiant" if r else "Dire"