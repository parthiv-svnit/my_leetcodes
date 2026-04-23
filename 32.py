class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack  = []
        valid = 0
        count1 = 0
        for i in range(len(s)):
            count = 0
            if not stack and s[i] == ')':
                valid = 0
                continue
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                stack.pop()
                count += 2
                if valid == 0:
                    count1 = count
                else :
                    count1 += count
                valid = 1
        return count1
    
a = Solution()
print(a.longestValidParentheses('()(()'))