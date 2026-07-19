class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        di = {0 : -1}
        out = 0

        for i, num in enumerate(nums) :
            if num == 0 :
                prefix -= 1
            else :
                prefix += 1
            if prefix in di :
                out = max(out, i - di[prefix])
            else :
                di[prefix] = i
        return out