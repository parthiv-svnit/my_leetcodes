class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return
        pivot = i
        
        mini = None
        for n in range(pivot + 1, len(nums)):
            if nums[n] > nums[pivot]:
                if mini is None or nums[n] < nums[mini]:
                    mini = n
        
        nums[pivot], nums[mini] = nums[mini], nums[pivot]

        nums[pivot + 1:] = sorted(nums[pivot + 1:])