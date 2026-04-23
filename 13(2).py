class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        num = {
            'M' : 1000 , 'D' : 500 , 'C' : 100 , 'L' : 50 , 'X' : 10 , 'V' : 5 , 'I' : 1
        }

        for i in range(len(s)):
            if i < len(s) - 1 and num[s[i]] < num[s[i+1]] :
                out -= num[s[i]]
            else :
                out += num[s[i]]
        return out