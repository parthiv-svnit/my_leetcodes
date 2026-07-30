class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = list(set(candyType))
        n = len(candyType)
        c = len(types)
        if c <= n // 2 :
            return c
        else :
            return n // 2