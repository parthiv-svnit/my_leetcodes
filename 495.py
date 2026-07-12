class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n = len(timeSeries)
        dp = [0] * n
        dp[0] = duration

        for i in range(1, n) :
            if timeSeries[i - 1] + duration - 1 >= timeSeries[i] :
                dp[i] = dp[i - 1] - timeSeries[i - 1] + timeSeries[i]
            else :
                dp[i] = dp[i - 1] + duration
        return dp[-1]