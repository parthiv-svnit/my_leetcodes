class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * 26
        temp = 0
        for i, ch in enumerate(s) :
            if ord(ch) - ord(s[i - 1]) == 1 or (ch == 'a' and s[i - 1] == 'z') :
                temp += 1
            else :
                temp = 1
            ind = ord(ch) - ord('a')
            dp[ind] = max(dp[ind], temp)
        return sum(dp)