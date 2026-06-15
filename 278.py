# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fun(i,j) :
            m = i + (j - i) // 2
            if isBadVersion(m) and not isBadVersion(m - 1) : 
                return m
            elif isBadVersion(m) :
                return fun(i, m - 1)
            else :
                return fun(m + 1, j)
        return fun(1, n)