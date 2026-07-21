class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def fun(t) :
            temp = t.split(":")
            return 60 * int(temp[0]) + int(temp[1])
        out = float('inf')
        arr = [fun(i) for i in timePoints]
        arr.sort()
        for i in range(len(arr) - 1) :
            out = min(out, arr[i + 1] - arr[i]) 
        out = min(out, 1440 - (arr[-1] - arr[0]))
        return out