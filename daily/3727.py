class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        out = 0
        nums = [abs(x) for x in nums]
        nums.sort()
        # print(nums)
        n = len(nums)
        for i in range(n // 2) :
            out -= nums[i] ** 2
        for i in range(n // 2, n) :
            out += nums[i] ** 2
        return out