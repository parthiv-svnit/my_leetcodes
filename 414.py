class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = float('-inf')
        m2 = float('-inf')
        m3 = float('-inf')
        nums = set(nums)
        if len(nums) < 3 :
            return max(nums)
        for i in nums :
            if i > m1 :
                m3 = m2
                m2 = m1
                m1 = i
            elif i > m2 :
                m3 = m2
                m2 = i
            elif i > m3 :
                m3 = i
        return m3