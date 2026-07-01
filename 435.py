class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x : x[1])
        n = len(intervals)
        i = 1
        out = 0
        temp = intervals[0][1]
        while i < n :
            if intervals[i][0] < temp :
                out += 1
            else :
                temp = intervals[i][1]
            i += 1
        return out