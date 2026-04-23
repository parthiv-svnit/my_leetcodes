class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums :
            return 0
        if nums[0] > target :
            return 0
        if nums[-1] < target :
            return len(nums)

        def fun(l,r,target) :
            
            if l > r :
                return l
            
            m = l + (r - l) // 2

            if nums[m] == target :
                return m
            elif nums[m] < target :
                return fun(m + 1, r, target)
            else :
                return fun(l, m - 1 , target)
        
        return fun(0, len(nums) - 1, target)