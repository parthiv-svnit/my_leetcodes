class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minv = float('inf')
        maxv = float('-inf')
        
        for i, v in enumerate(nums) :
            if v < minv :
                minv = v
                mini = i
            if v > maxv :
                maxv = v
                maxi = i
        if abs(n // 2 - mini) < abs(n // 2 - maxi) :
            mini, maxi = maxi, mini
            minv, maxv = maxv, minv
        print(mini, minv)
        print(maxi, maxv)
        out = 0
        out += min(mini + 1, n - mini)
        print(out)
        l = 0
        r = n - 1
        if mini < n // 2 :
            l = mini + 1
        else :
            r = mini - 1
        out += min(maxi - l + 1, r + 1 - maxi)
        return out