class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 4000 or num <= 0:
            return None
        out = []
        while num > 0:
            if num >= 1000:
                out.append('M')
                num -= 1000
            elif num >= 500:
                if num >= 900:
                    out.append('CM')
                    num -= 900
                else:
                    out.append('D')
                    num -= 500
            elif num >= 100:
                if num >= 400:
                    out.append('CD')
                    num -= 400
                else:
                    out.append('C')
                    num -= 100
            elif num >= 50:
                if num >= 90:
                    out.append('XC')
                    num -= 90
                else:
                    out.append('L')
                    num -= 50
            elif num >= 10:
                if num >= 40:
                    out.append('XL')
                    num -= 40
                else:
                    out.append('X')
                    num -= 10
            elif num >= 5:
                if num >= 9:
                    out.append('IX')
                    num -= 9
                else:
                    out.append('V')
                    num -= 5
            else:
                if num >= 4:
                    out.append('IV')
                    num -= 4
                else:
                    out.append('I')
                    num -= 1
        return "".join(out)

a = Solution()
print(a.intToRoman(1994))