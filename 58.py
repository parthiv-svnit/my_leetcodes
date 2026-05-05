class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        j = len(s) - 1
        while s[j] == ' ' :
            j -= 1
        for i in range (j, -1, -1) :
            if s[i] == ' ':
                break
            out += 1
        return out