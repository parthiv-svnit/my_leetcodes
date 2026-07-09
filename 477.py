class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        out = 0
        for i in range(32) :
            o = 0
            for num in nums :
                o += (num >> i) & 1
            out += o * (n - o)
        return out