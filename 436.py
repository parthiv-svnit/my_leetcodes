class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        out = [-1] * n
        di = {}
        for i, val in enumerate(intervals) :
            di[val[0]] = i
        intervals = sorted(intervals, key = lambda x : x[0])
        for i in range(n) :
            tempi = bisect_left(intervals, intervals[i][1], key = lambda x : x[0])
            if tempi != n :
                out[di[intervals[i][0]]] = di[intervals[tempi][0]]
        return out