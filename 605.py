class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ln = len(flowerbed)
        if not n :
            return True
        if ln == 1 :
            return not flowerbed[0]
        if flowerbed[0] == 0 and flowerbed[1] == 0 :
            n -= 1
            flowerbed[0] = 1
        if not n :
            return True
        if flowerbed[-1] == 0 and flowerbed[-2] == 0 :
            n -= 1
            flowerbed[-1] = 1
        if not n :
            return True
        
        for i in range(1, ln - 1) :
            if not flowerbed[i] :
                if not flowerbed[i - 1] and not flowerbed[i + 1] :
                    n -= 1
                    flowerbed[i] = 1
        return n <= 0
            