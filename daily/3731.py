class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        i, j = nums[0], nums[-1]
        k = 0
        out = []
        print(nums)
        i1 = i
        while i1 < j + 1 :
            if nums[k] != i1 :
                out.append(i1)
                k -= 1
            i1 += 1
            k += 1
        return out