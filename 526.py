class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False] * (n + 1)
        out = [0]

        def fun(pos) :
            if pos > n :
                out[0] += 1
                return
            for num in range(1, n + 1) :
                if not used[num] and (num % pos == 0 or pos % num == 0) :
                    used[num] = True
                    fun(pos + 1)
                    used[num] = False
        fun(1)
        return out[0]