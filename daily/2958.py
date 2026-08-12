class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        out = 0
        n = len(nums)
        fr = defaultdict(int)
        for j in range(n) :
            fr[nums[j]] += 1
            while fr[nums[j]] > k :
                fr[nums[i]] -= 1
                i += 1
            out = max(out, j - i + 1)
        return out