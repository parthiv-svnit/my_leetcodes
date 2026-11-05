class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        out = 0
        mn = min(arr2)
        mx = max(arr2)
        for i in arr1 :
            if abs(mx - i) <= d or abs(mn - i) <= d :
                continue
            for j in arr2 :
                if abs(j - i) <= d :
                    break
            else :
                out += 1
            
        return out