from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        di = Counter(nums)
        di = sorted(di.items(), key = lambda item : item[1], reverse = True)
        return [x for x, _ in di[:k]]