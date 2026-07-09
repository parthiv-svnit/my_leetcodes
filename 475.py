class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        out = 0
        for i in houses :
            ind = bisect_left(heaters, i)

            l = float('inf')
            r = float('inf')

            if ind > 0 :
                l = i - heaters[ind - 1]
            if ind < len(heaters) :
                r = heaters[ind] - i
            
            out = max(out, min(l, r))
        return out