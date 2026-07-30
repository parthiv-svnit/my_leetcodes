class Solution:
    def maxProduct(self, n: int) -> int:
        m1 = -1
        m2 = -1
        while n > 0 :
            i = n % 10
            if i >= m1 :
                m2 = m1
                m1 = i
            elif i > m2 :
                m2 = i
            n //= 10
        return m1 * m2