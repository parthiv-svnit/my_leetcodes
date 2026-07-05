class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[0])

        ls, le = points[0]
        out = 1
        for s, e in points[1:] :
            if s <= le :
                le = min(le, e)
            else :
                out += 1
                le = e
        return out