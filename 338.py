class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out = []
        for i in range(n + 1) :
            out.append(sum(list(map(int, format(i, 'b')))))
        return out