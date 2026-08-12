class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = 1
        n = len(nums)
        out = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1 :
            out += nums[i]
            i += 1
        nums = set(nums)
        while out in nums :
            out += 1
        return out