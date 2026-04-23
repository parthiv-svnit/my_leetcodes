class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        dividend, divisor = abs(dividend), abs(divisor)

        count = 0

        while dividend >= divisor: 
            temp = divisor
            quo = 1
            while dividend >= (temp << 1) :
                temp <<= 1
                quo <<= 1
            dividend = dividend - temp
            count += quo
        
        if sign*count > 2**31 - 1:
            return 2**31 - 1
        elif sign*count < -2**31:
            return -2**31

        return sign*count