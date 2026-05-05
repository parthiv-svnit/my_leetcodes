class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        out = [intervals[0]]

        for s,e in intervals :
            ls,le = out[-1]
            if s <= le :
                out[-1] = ls, max(le, e)
            else :
                out.append([s,e])

        return out