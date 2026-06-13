class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9 :
            t = num
            num = 0
            while t > 0 :
                num += t % 10
                t //= 10
        return num