class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        di = defaultdict(int)

        for i in wall :
            pos = 0
            for j in i[:-1] :
                pos += j
                di[pos] += 1
        return len(wall) - max(di.values(), default = 0)