class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        d = nums[n // 2]
        out = 0
        for i in nums :
            out += abs(i - d)
        return out