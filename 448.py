class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di = defaultdict(int)
        out = []
        n = len(nums)
        for i in nums :
            di[i] += 1
        for i in range(1, n + 1) :
            if di[i] == 0 :
                out.append(i)
        return out