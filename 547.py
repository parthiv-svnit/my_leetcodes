class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        out = 0
        def fun(city) :
            visited[city] = True
            for ne in range(n) :
                if isConnected[city][ne] and not visited[ne] :
                    fun(ne)
        for city in range(n) :
            if not visited[city] :
                fun(city)
                out += 1
        return out