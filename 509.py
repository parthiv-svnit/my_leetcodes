class Solution:
    def fib(self, n: int) -> int:
        dp = []
        i = 1
        dp.append(0)
        if n == 0 :
            return 0
        dp.append(1)
        while i < n :
            dp.append(dp[-1] + dp[-2])
            i += 1
        return dp[-1]