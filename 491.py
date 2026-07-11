class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        path = []
        def fun(ind) :
            if len(path) >= 2 :
                out.append(path[:])
            used = set()
            for i in range(ind, len(nums)) :
                if nums[i] in used :
                    continue
                if path and nums[i] < path[-1] :
                    continue
                used.add(nums[i])
                path.append(nums[i])
                fun(i + 1)
                path.pop()
        fun(0)
        return out