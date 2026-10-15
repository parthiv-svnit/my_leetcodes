class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        out = 0
        n = len(nums)
        for i in range(n) :
            s = set()
            for j in range(i, n) :
                s.add(nums[j])
                out += len(s) ** 2
        return out