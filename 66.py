class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        no = int("".join(map(str, digits)))

        no = no + 1

        return [int(d) for d in str(no)]