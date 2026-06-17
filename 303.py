class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0]
        for i in nums :
            self.arr.append(self.arr[-1] + i)
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.arr[right + 1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)