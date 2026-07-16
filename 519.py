class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = self.m * self.n
        self.matrix = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        i = random.randint(0, self.total - 1)
        x = self.matrix.get(i, i)
        self.total -= 1
        self.matrix[i] = self.matrix.get(self.total, self.total)
        return [x // self.n, x % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.matrix.clear()
        self.total = self.m * self.n

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()