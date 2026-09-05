class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        print(nums)
        n = len(nums)
        maxi = nums[0]
        mini = min(nums)
        if maxi - mini <= k :
            return 0
        for i in range(1, n) :
            maxi = max(maxi, nums[i])
            if nums[i - 1] == mini :
                mini = min(nums[i:])
            if maxi - mini <= k :
                return i
        return -1