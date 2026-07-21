class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 1 :
            return nums[0]
        i = 0
        while i < n - 1 : 
            x = i
            while i < n - 1 and nums[i] == nums[i + 1] :
                i += 1
            if i == x :
                return nums[i]
            i += 1
        return nums[-1]