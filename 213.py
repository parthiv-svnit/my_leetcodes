class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1 :
            return nums[0]
            
        def fun(i, j) :
            m = 0
            n = 0
            for k in range(i, j + 1) :
                o = max(m, n + nums[k])
                n = m
                m = o
            return m
        return max(fun(0, n - 2), fun(1, n - 1))