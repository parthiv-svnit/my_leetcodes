class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        out = [0] * len(queries)
        logs.sort(key = lambda x: x[1])
        indexed_queries = sorted(enumerate(queries), key = lambda x: x[1])
        di = Counter()
        j = 0
        k = 0
        for i, q in indexed_queries :
            l = q - x
            r = q
            while k < len(logs) and logs[k][1] <= r :
                di[logs[k][0]] += 1
                k += 1
            while j < len(logs) and logs[j][1] < l :
                server = logs[j][0]
                di[server] -= 1
                if di[server] == 0 :
                    del di[server]
                j += 1
            out[i] = n - len(di)
            
        return out