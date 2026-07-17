class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rindex = {0 : -1}
        prefix = 0

        for i, num in enumerate(nums) :
            prefix += num
            r = prefix % k
            
            if r in rindex :
                if i - rindex[r] >= 2 :
                    return True
            else :
                rindex[r] = i
        return False