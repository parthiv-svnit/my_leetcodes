class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [0] * n
        s = sum(nums)
        for j, v in enumerate(nums) :
            f[0] += j * v
        out = f[0]
        for i in range(1, n) :
            f[i] = f[i - 1] + s - n * nums[n - i]
            out = max(out, f[i])
        return out