class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = float('inf')
        m2 = float('inf')
        for i in nums :
            if i <= m1 :
                m1 = i
            elif i <= m2 :
                m2 = i
            else :
                return True
        return False