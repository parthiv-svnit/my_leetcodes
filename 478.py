class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.h = x_center
        self.k = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True :
            x = random.uniform(self.h - self.r, self.h + self.r)
            y = random.uniform(self.k - self.r, self.k + self.r)
            if (x - self.h) ** 2 + (y - self.k) ** 2 <= (self.r) ** 2 :
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()