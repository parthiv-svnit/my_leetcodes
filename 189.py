class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [i for i in nums]
        for i in range(n) :
            nums[(i + k) % n] = temp[i]