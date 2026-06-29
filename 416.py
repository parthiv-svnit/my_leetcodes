class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sn = sum(nums)
        if sn & 1 :
            return False
        aim = sn // 2
        dp = [False] * (aim + 1)
        dp[0] = True
        for i in nums :
            for j in range(aim, i - 1, -1) :
                dp[j] = dp[j] or dp[j - i]
        return dp[-1]