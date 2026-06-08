class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st = {}
        ts = {}
        for i, j in zip(s, t) :
            if i in st and st[i] != j :
                return False
            if j in ts and ts[j] != i :
                return False
            st[i] = j
            ts[j] = i
        return True