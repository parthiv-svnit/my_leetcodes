class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        s = 0
        out = len(nums) + 1
        for i in range(len(nums)) :
            r = i
            s += nums[r]
            while s >= target :
                out = min(out, r - l + 1)
                s -= nums[l]
                l += 1
        if out == len(nums) + 1 :
            return 0
        return out