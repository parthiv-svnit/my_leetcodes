class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c ** 0.5) + 1) :
            b = c - a * a
            if b ** 0.5 == int(b ** 0.5) :
                return True
        return False