class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mini = m
        minj = n
        for i, j in ops :
            mini = min(mini, i)
            minj = min(minj, j)
        return mini * minj