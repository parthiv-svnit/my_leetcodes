class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()[::-1]
        out = []
        for i in range(0, len(s), k) :
            out.append(s[i: i+k])
        return '-'.join(s[::-1] for s in out[::-1])