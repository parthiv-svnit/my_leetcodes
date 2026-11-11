class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # if costBoth <= cost1 and costBoth <= cost2 :
        #     return costBoth * max(need1, need2)
        # elif costBoth < cost1 :
        #     return costBoth * (need1) + (max(0, (need2 - need1) * cost2))
        # elif costBoth < cost2 :
        #     return costBoth * (need2) + (max(0, (need1 - need2) * cost1))
        return min(((cost1 * need1) + (cost2 * need2)), ((costBoth * min(need1, need2)) + (max(0, (need1 - need2) * cost1)) + (max(0, (need2 - need1) * cost2))), (costBoth * max(need1, need2)))