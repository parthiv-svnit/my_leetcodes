class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        out = 0
        for i in nums :
            out ^= i
        if out != 0 :
            return n
        for i in nums :
            if i != 0 :
                return n - 1
        
        return 0