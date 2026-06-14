class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = []
        out.append(1)
        i2 = i3 = i5 = 0

        while len(out) < n :
            out.append(min(out[i2] * 2, out[i3] * 3, out[i5] * 5))
            if out[-1] == out[i2] * 2 :
                i2 += 1
            if out[-1] == out[i3] * 3 :
                i3 += 1
            if out[-1] == out[i5] *  5:
                i5 += 1
        return out[-1]