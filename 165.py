class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a1 = version1.split(".")
        a2 = version2.split(".")

        n = max(len(a1), len(a2))
        for i in range(n) :
            v1 = int(a1[i]) if i < len(a1) else 0
            v2 = int(a2[i]) if i < len(a2) else 0
            if v1 < v2 :
                return -1
            if v1 > v2 :
                return 1
        return 0