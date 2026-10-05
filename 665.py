class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n - 1) :
            if nums[i] > nums[i + 1] :
                count += 1
                if count > 1 :
                    return False
                if not i or nums[i - 1] <= nums[i + 1] :
                    nums[i] = nums[i + 1]
                else :
                    nums[i + 1] = nums[i]
        return True