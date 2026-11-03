class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        out = 0
        for i in nums :
            out += mx - i
        return out