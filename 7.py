class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        arr = int(str(x)[::-1])
        if sign*arr < -2**31 or sign*arr > 2**31-1:
            return 0
        return sign*arr
    
a = Solution()
print(a.reverse(1234567890))