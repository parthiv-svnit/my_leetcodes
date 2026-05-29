class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s :
            return s
        s = " " + s
        i = 0
        j = 0
        out = []
        while i < len(s) :
            if s[i] == " " :
                while i < len(s) and s[i] == " " :
                    i += 1
                if i < len(s) :
                    out.append(s[i])
                    j = len(out) - 1
            else : 
                out[j] += s[i]
            i += 1
        return " ".join(out[::-1])