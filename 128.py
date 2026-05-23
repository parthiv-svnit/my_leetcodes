class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = set(nums)
        streak = 0
        for n in snums :
            if n - 1 not in snums :
                startn = n
                count = 1

                while (startn + 1) in snums :
                    count += 1
                    startn += 1

                streak = max(streak, count)
        return streak