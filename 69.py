class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def sqrt(x, l, r) :
            if l > r :
                return r
            m = (l + r) // 2
            msq = m ** 2
            
            if msq > x :
                return sqrt(x, l, m - 1)
            elif msq < x :
                return sqrt(x, m + 1, r)
            else :
                return m

        return sqrt(x, 0, x)