class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n0 = 9
        i = 0
        arr = []
        arr.append(n0)
        while n0 < n :
            i += 1
            n0 = 9 * (10 ** i)
            if sum(arr) < n :
                arr.append(n0)
        
        j = 1
        i = 0
        while i < len(arr) - 1 :
            temp = j * arr[i]
            if n > temp :
                n -= temp
            else :
                break
            j += 1
            i += 1
       
        if n % j != 0 :
            ind = (n % j) - 1
            n //= j
            n += sum(arr[:j-1]) + 1
            return int(str(n)[ind])
        
        n //= j
        n += sum(arr[:j-1])
        return n % 10