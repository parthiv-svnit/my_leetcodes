class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False
        d1 = {}
        for i in s :
            if i in d1 :
                d1[i] += 1
            else :
                d1[i] = 1

        for i, j in d1.items() :
            if t.count(i) != j :
                return False
        return True