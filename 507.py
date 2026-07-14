class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 :
            return False
        arr = set()
        arr.add(1)
        for i in range(2, int(num ** 0.5) + 1) :
            if num % i == 0 :
                arr.add(i)
                arr.add(num // i)
        
        temp = 0
        for i in arr :
            temp += i
        return temp == num