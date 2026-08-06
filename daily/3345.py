class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def fun(n) :
            temp = 1
            while n > 0 :
                temp *= n % 10
                n //= 10
            return temp

        while True :
            if not fun(n) % t :
                return n
            n += 1