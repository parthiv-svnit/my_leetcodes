class Solution:
    def minSteps(self, n: int) -> int:
        d = 2
        out = 0
        while n > 1 :
            while n % d == 0 :
                out += d
                n //= d
            d += 1
        return out