class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        out = float('inf')
        for i in range(n) :
            temp = 0
            for j in range(i, n) :
                temp += nums[j]
                if l <= j - i + 1 <= r and temp > 0 :
                    out = min(out, temp)
        return out if out != float('inf') else -1