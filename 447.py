class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        out = 0
        for x1, y1 in points :
            f = defaultdict(int)
            for x2, y2 in points :
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                f[d] += 1
            for i in f.values() :
                out += i * (i - 1)
        return out