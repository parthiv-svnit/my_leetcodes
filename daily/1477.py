class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        dp = [float('inf')] * n
        l = 0
        temp = 0
        out = float('inf')
        for r in range(n) :
            temp += arr[r]
            while temp > target :
                temp -= arr[l]
                l += 1

            if temp == target :
                length = r - l + 1
                if l > 0 and dp[l - 1] != float('inf') :
                    out = min(out, length + dp[l - 1])
                dp[r] = min(dp[r], length)
            if r > 0 :
                dp[r] = min(dp[r], dp[r - 1])
        return -1 if out == float('inf' ) else out