class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = float('-inf')
        r = -1
        for i in range(n) :
            max1 = max(max1, nums[i])
            if nums[i] < max1 :
                r = i
        min1 = float('inf')
        l = -1
        for i in range(n - 1, -1, -1) :
            min1 = min(min1, nums[i])
            if nums[i] > min1 :
                l = i
        if r == -1 :
            return 0
        return r - l + 1