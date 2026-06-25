class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out = list(range(1, n + 1))
        out = map(str, out)
        out = map(int, sorted(out))
        return out