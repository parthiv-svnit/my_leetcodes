class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s :
            return True

        l = 0
        r = len(s) - 1
        
        while l < r :
            while l < r and not ( ( 'a' <= s[l].lower() <= 'z' ) or ( '0' <= s[l] <= '9' ) ) :
                l += 1             
            while l < r and not ( ( 'a' <= s[r].lower() <= 'z' ) or ( '0' <= s[r] <= '9' ) ) :
                r -= 1             
            if s[l].lower() != s[r].lower() :
                return False
            l += 1
            r -= 1
        return True