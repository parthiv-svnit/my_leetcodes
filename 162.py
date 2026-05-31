class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 0
        if len(nums) == 2 :
            return 0 if nums[0] > nums[1] else 1
        for i in range(1, len(nums) - 1) :
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i] :
                return i
        if nums[0] > nums[1] :
            return 0
        if nums[-1] > nums[-2] :
            return len(nums) - 1