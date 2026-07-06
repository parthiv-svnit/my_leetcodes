class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a3 = float('-inf')
        stack = []
        for i in reversed(nums) :
            if i < a3 :
                return True
            while stack and stack[-1] < i :
                a3 = stack.pop()
            stack.append(i)
        return False