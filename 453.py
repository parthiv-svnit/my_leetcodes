class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi = min(nums)
        out = 0
        for i in nums :
            out += i - mi
        return out