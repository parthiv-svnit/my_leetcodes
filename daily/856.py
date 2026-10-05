class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s :
            if i == '(' :
                stack.append(0)
            else :
                x = stack.pop()
                if not x :
                    x = 1
                else :
                    x = 2 * x
                print(stack)
                stack[-1] += x
        return stack[-1]