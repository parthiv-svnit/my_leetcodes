class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 1 if nums[0] == 1 else 0
        out = 0
        i = 0
        while i < len(nums) :
            if nums[i] != 1 :
                i += 1
                continue
            if i == len(nums) - 1 :
                m1 = 1
                out = max(out, m1)
                break
            m1 = 1
            while i < len(nums) - 1 and nums[i + 1] == 1 :
                m1 += 1 
                i += 1
            i += 1
            out = max(out, m1)
        return out