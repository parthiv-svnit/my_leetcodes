class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2 :
            num2 = '0' * (n1 - n2) + num2
        elif n2 > n1 :
            num1 = '0' * (n2 - n1) + num1
        i = max(n1, n2) - 1
        c = 0
        out = ''
        def fun(n) :
            return ord(n) - ord('0')
        while i >= 0:
            temp = fun(num1[i]) + fun(num2[i]) + c
            if temp > 9:
                temp = temp - 10
                c = 1
            else:
                c = 0
            out = str(temp) + out
            i -= 1
        if c == 1:
            out = '1' + out      
        return out