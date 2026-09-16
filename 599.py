class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        di = {}
        for i, j in enumerate(list1) :
            di[j] = i
        out = float('inf')
        out1 = 0
        out0 = []
        # print(di)
        for i, j in enumerate(list2) :
            if j in di :
                # print(i, j)
                x = di[j] + i
                if x < out :
                    out = x
                    out1 = j
                    out0 = []
                    out0.append(out1)
                elif x == out :
                    out = x
                    out1 = j
                    out0.append(out1)
                    
        return out0