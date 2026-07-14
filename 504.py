class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0 :
            return "0"
        temp = abs(num)
        out = []
        arr = []
        x = 0
        for i in range(9) :
            x = 7 ** i
            if x > temp :
                break
            arr.append(x)
            
        for i in reversed(arr) :
            out.append(temp // i)
            temp = temp % i

        return ''.join(map(str, out)) if num >= 0 else '-' + ''.join(map(str, out))