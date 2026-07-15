class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        
        di = defaultdict(list)

        for i, ch in enumerate(ring) :
            di[ch].append(i)

        @cache
        def fun(i, cur) :
            if i == len(key) :
                return 0
            out = float('inf')

            for nxt in di[key[i]] :
                dist = abs(nxt - cur)
                step = min(dist, n - dist)
                out = min(out, step + 1 + fun(i + 1, nxt))
            return out
        return fun(0, 0)