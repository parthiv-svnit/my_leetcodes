class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = []
        n = len(nums)
        di = Counter(nums)
        out0 = [i for i, j in di.items() if j == 2]
        out1 = (n * (n + 1) // 2) + out0[0] - sum(nums)
        return out0[0], out1