class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        out = []
        ns, ne = newInterval[0], newInterval[1]
        ni, nj = 0, len(intervals) - 1
        
        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if ns <= e :
                ni = i
                break
            out.append([s,e])
        if ni > len(intervals) - 1 :
            out.append([ns, ne])
            return out
        if len(out) == len(intervals):
            out.append([ns,ne])
            return out
        for i in range(ni, len(intervals)) :
            s = intervals[i][0]
            e = intervals[i][1]

            if ne < s :
                nj = i - 1
                break
        if nj < 0 :
            out.append([ns, ne])
        
        else :
            out.append([min(ns, intervals[ni][0]), max(ne, intervals[nj][1])])

        for i in range(nj + 1, len(intervals)) :
            s = intervals[i][0]
            e = intervals[i][1]
            out.append([s,e])

        return out