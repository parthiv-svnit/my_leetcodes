class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        arr = set()
        for i in nums :
            if i in seen :
                arr.add(i)
            seen.add(i)
        
        for a in arr :
            ind = [i1 for i1, j in enumerate(nums) if j == a]
            i = 0
            j = 1

            while j < len(ind) :
                if ind[j] - ind[i] <= k :
                    return True
                i += 1
                j += 1
        return False