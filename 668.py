class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n :
            m, n = n, m
        l = 1
        h = m * n
        while  l < h :
            mid = (l + h) // 2
            count = 0
            for i in range(1, m + 1) :
                count += min(n, mid // i)
            if count < k :
                l = mid + 1
            else :
                h = mid
        return l