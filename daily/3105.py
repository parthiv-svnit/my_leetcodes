class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i = 1
        d = 1

        out = 0
        n = len(nums)
        if n < 2 :
            return 1
        for j in range(n - 1) :
            if nums[j] < nums[j + 1] :
                i += 1
                d = 1
            elif nums[j] > nums[j + 1] :
                d += 1
                i = 1
            else :
                i = 1
                d = 1
            out = max(out, i, d)
            # print(out, i, d)
        return out