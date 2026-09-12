class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0 : k])
        print(s)
        n = len(nums)
        temp = s
        for i in range(k, n) :
            temp -= nums[i - k]
            temp += nums[i]
            s = max(s, temp)
        return s / k