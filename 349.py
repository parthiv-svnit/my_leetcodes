class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        out = []
        while i < n1 and j < n2 :
            if nums1[i] == nums2[j] :
                out.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j] :
                i += 1
            else :
                j += 1
        return out