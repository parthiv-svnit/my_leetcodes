class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        j = 0
        cj = 0
        dist = 0
        for i in range(len(nums)):
            dist = max(dist, i + nums[i])
            if i == cj:
                j += 1
                cj = dist
                if cj >= len(nums) - 1:
                    return j