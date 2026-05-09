class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for c in nums :
            if c == 0 :
                zero += 1
            elif c == 1 :
                one += 1
            elif c == 2 :
                two += 1
        nums[:] = [0] * zero + [1] * one + [2] * two