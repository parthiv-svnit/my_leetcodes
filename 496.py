class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        stac = []
        for i in reversed(nums2) :
            if not stac :
                dic[i] = -1
            elif stac[-1] < i :
                stac.pop()
                while stac and stac[-1] < i :
                    stac.pop()
                if stac :
                    dic[i] = stac[-1]
                else :
                    dic[i] = -1
            else :
                dic[i] = stac[-1]
            stac.append(i)
        return [dic[i] for i in nums1]