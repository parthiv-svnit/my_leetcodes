class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 0
        nums.sort()
        mx = 0
        for i in range(len(nums) - 1) :
            mx = max(mx, nums[i + 1] - nums[i])
        return mx