import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.di = {}
        for i in range(len(nums)) :
            if nums[i] in self.di :
                self.di[nums[i]].append(i)
            else :
                self.di[nums[i]] = [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.di[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)