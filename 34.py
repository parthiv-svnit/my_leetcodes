class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1

        if not nums :
            return -1,-1
        while nums[i] <= target and nums[j] >= target: 
            if nums[i] < target :
                i += 1
            if nums[j] > target :
                j -= 1
            if nums[i] == nums[j] == target :
                return i,j
        return -1,-1