class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        nums.sort()
        out = nums[0] + nums[1] + nums[2]
        if len(nums) == 3:
            return out
            
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k :
                sum = nums[i] + nums[j] + nums[k]
                if abs(out - target) > abs(sum - target):
                    out = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return out
    
a = Solution()
print(a.threeSumClosest([1,2,3,4],6))