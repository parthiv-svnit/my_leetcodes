class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] in ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()

            elif s[i] in '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            
            elif s[i] in ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0