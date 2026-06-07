class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True :
            k = 0
            while n > 0 :
                k += (n % 10)**2 
                n //= 10
            if k in seen :
                return False
            if k == 1 :
                return True
            n = k
            seen.add(k)