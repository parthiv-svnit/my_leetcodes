class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def fun(s, t) :
            i = 0
            for c in t :
                if i < len(s) and s[i] == c :
                    i += 1
            return i == len(s)
        out = -1

        for i in range(len(strs)) :
            ok = True
            for j in range(len(strs)) :
                if i == j :
                    continue
                if fun(strs[i], strs[j]) :
                    ok = False
                    break
            if ok :
                out = max(out, len(strs[i]))
        return out