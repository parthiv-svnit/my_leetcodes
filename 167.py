class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)) :
            if i > 0 and numbers[i] in numbers[:i] :
                continue
            if target - numbers[i] in numbers[i+1:] :
                return i + 1, numbers[i+1:].index(target - numbers[i]) + i + 2
            