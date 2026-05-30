class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minp = maxp = out = nums[0]

        for i in range(1,len(nums)) :
            if nums[i] < 0 :
                maxp, minp = minp, maxp
            maxp = max(nums[i], maxp * nums[i])
            minp = min(nums[i], minp * nums[i])

            out = max(out, maxp)
        return out