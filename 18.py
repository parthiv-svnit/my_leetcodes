class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l :
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        out.append([nums[i], nums[j], nums[k], nums[l]])

                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        
                        k += 1
                        l -= 1
        return out
    
a = Solution()
print(a.fourSum([1,2,4,3,4,4],10))