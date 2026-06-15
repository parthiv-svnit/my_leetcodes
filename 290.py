class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        w = s.split()
        if len(w) != len(pattern) :
            return False
        ps = {}
        sp = {}

        for i, j in zip(w, pattern) :
            if i in ps and ps[i] != j :
                return False
            if j in sp and sp[j] != i :
                return False
            ps[i] = j
            sp[j] = i
        return True