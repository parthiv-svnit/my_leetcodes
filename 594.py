class Solution:
    def findLHS(self, nums: List[int]) -> int:
        di = Counter(nums)
        di = dict(sorted(di.items(), key = lambda x : x[0]))
        nums.sort()
        print(nums, di)
        n = len(nums)
        out = 0
        for i in range(1, n) :
            if nums[i - 1] == nums[i] - 1 :
                out = max(out, di[nums[i - 1]] + di[nums[i]])
        return out