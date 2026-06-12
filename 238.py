class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 1
        n = len(nums)
        for i in range(n) :
            a = a * nums[i]
            if a == 0 :
                break
        out = [0] * n
        if a == 0 :
            if nums.count(0) > 1 :
                return out
            else :
                a = 1
                for i in range(n) :
                    if nums[i] == 0 :
                        continue
                    a = a * nums[i]
                out[nums.index(0)] = a
            
        else :
            for i in range(n) :
                out[i] = a // nums[i]
        return out