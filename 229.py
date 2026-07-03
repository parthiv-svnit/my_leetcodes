class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di = Counter(nums)
        out = []
        n = len(nums)
        k = n // 3
        for x, y in di.items() :
            if y > k :
                out.append(x)
        return out