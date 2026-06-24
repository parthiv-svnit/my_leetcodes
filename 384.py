import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.nums1 = self.nums[:]   

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums1
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()