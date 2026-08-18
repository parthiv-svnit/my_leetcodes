class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        out = -1
        n = len(nums)
        if k == 1 :
            for i in set(nums) :
                if nums.count(i) == 1 :
                    out = max(out, i)
            return out
        if k == n :
            return max(nums)
        if nums[0] not in nums[1:] :
            out = nums[0]
        if nums[-1] not in nums[: n - 1] :
            out = max(out, nums[-1])
        return out