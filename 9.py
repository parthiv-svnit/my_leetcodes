class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = len(str(x))
        for i in range(n // 2):
            if str(x)[i] == str(x)[n - i - 1]:
                continue
            else:
                return False
        return True

a = Solution()
print(a.isPalindrome(123321))