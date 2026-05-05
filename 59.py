class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        out = [[0] * n for _ in range(n)]
        num = 1
        t = 0
        d = n - 1
        l = 0
        r = n - 1

        while l <= r and t <= d :
            count = l
            while count <= r :
                out[t][count] = num
                num += 1
                count += 1
            t += 1
            count = t
            while count <= d :
                out[count][r] = num
                num += 1
                count += 1
            r -= 1
            if t <= d :
                count = r
                while count >= l :
                    out[d][count] = num
                    num += 1
                    count -= 1
                d -= 1
            if l <= r :
                count = d
                while count >= t :
                    out[count][l] = num
                    num += 1
                    count -= 1
                l += 1

        return out