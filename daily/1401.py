class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter < x2 :
            x = max(xCenter, x1)
        else :
            x = x2
        
        if yCenter < y2 :
            y = max(yCenter, y1)
        else :
            y = y2
        
        return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2