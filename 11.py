class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max = 0

        while i < j :
            a = (j-i) * (min(height[i],height[j]))
            if a > max:
                max = a
            if height[i] <= height[j]:
                i += 1
            else:
                j-=1
            
        return max