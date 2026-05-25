class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0

        for i in range(32) :
            count = 0

            for n in nums :
                count += (n >> i) & 1
            count %= 3
            
            if i == 31 and count == 1 :
                out -= (1 << i)
            else :
                out |= (count << i)
        return out      