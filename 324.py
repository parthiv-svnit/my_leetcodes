class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid = (n + 1) // 2
        nums.sort()
        l = nums[:mid]
        r = nums[mid:]

        for i in range(n) :
            if i % 2 == 0 :
                nums[i] = l.pop()
            else :
                nums[i] = r.pop()