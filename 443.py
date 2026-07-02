class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        temp = 1
        i = 1
        while i < len(chars) :
            temp = 1
            if chars[i] == chars[i - 1] :
                j = i
                while i < len(chars) and chars[i] == chars[i - 1] :
                    temp += 1
                    i += 1
                chars[j:j] = str(temp)
                del chars[j + len(str(temp)): j + temp + len(str(temp)) - 1]
                i = j + len(str(temp))
            i += 1
        return len(chars)