class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        arr = []
        i=0
        sign = 1
        Max = 2**31 - 1
        Min = -2**31

        if s[0] == '-':
            sign = -1
            i+=1
        elif s[0] == '+':
            i+=1

        for j in range(i,len(s)):
            if s[j].isdigit():
                arr.append(s[j])
            else:
                break

        if not arr:
            return 0
        out = sign * int("".join(arr))
        if out > Max:
            out = Max
        elif out < Min:
            out = Min
        return out

a = Solution()
print(a.myAtoi('-1455b2b33b333'))