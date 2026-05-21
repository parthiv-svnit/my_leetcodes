class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = prices[0]
        pro = 0
        for i in range(1, len(prices)) :
            if prices[i] <= minp :
                minp = prices[i]
            else :
                pro = max(pro, prices[i] - minp)
        return pro