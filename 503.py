class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [-1] * n
        stac = []
        for i in range(2 * n, -1, -1) :
            ind = i % n

            while stac and stac[-1] <= nums[ind] :
                stac.pop()
            if i < n :
                if stac :
                    out[ind] = stac[-1]
            stac.append(nums[ind])
        return out