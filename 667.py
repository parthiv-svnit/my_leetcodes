class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        out = []
        for i in range(1, n - k) :
            out.append(i)
        l, r = n - k, n
        for i in range(k + 1) :
            if i % 2 == 0 :
                out.append(l)
                l += 1
            else :
                out.append(r)
                r -= 1
        return out