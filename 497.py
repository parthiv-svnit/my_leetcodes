class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix = []
        total = 0
        for i in rects :
            total += (i[2] - i[0] + 1) * (i[3] - i[1] + 1)
            self.prefix.append(total)

    def pick(self):
        """
        :rtype: List[int]
        """
        ran = random.randint(1, self.prefix[-1])
        ind = bisect.bisect_left(self.prefix, ran)
        
        i = self.rects[ind]
        return [random.randint(i[0], i[2]), random.randint(i[1], i[3])]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()