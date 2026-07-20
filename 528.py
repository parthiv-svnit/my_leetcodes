class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = []
        self.prefix.append((self.w)[0])
        for i in range(1, len(self.w)) :
            self.prefix.append(self.prefix[-1] + self.w[i])
        print(self.prefix)

    def pickIndex(self) -> int:
        x = random.randint(1, self.prefix[-1])
        return bisect_left(self.prefix, x)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()