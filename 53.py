class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        msum = nums[0]
        csum = 0

        for n in nums:
            if csum < 0:
                csum = 0
            csum += n

            if msum < csum :
                msum = csum
        return msum