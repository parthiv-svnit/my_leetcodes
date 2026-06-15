class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = []
        for i in nums :
            if i != 0 :
                arr.append(i)
        nums[:] = arr
        nums.extend([0] * (n - len(arr)))