class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def fun(n) :
            out = 0
            while n > 0 :
                out += n % 10
                n //= 10
            return out
        n = len(nums)
        for i in range(n) :
            if fun(nums[i]) == i :
                return i
        return -1