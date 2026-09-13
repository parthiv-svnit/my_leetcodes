class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        di = {}
        def fun(needs) :
            if tuple(needs) in di :
                return di[tuple(needs)]

            out = 0
            for i, j in zip(price, needs) :
                out += i * j
            print(out)
            ln = len(special[0])
            for i in special :
                check = True
                for j in range(ln - 1) :
                    if i[j] > needs[j] :
                        check = False
                        break
                if check :
                    newneed = []
                    for k in range(ln - 1) :
                        newneed.append(needs[k] - i[k])
                    cost = i[-1] + fun(newneed)
                    out = min(out, cost)
            di[tuple(needs)] = out
            return out
        return fun(needs)