class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        i, j = 0, 1
        n = len(nums)
        nums.sort()
        out = set()
        print(nums)
        while i < len(nums) - 1 and j < len(nums) :
            if nums[j] - nums[i] < k :
                j += 1
                if j == len(nums) :
                    break
            elif nums[j] - nums[i] > k :
                if i == j - 1 :
                    j += 1
                else :
                    i += 1
                if j == len(nums) :
                    break
            else :
                out.add((nums[i], nums[j]))
                j += 1
        
        return len(out)