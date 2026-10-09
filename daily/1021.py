class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = 0
        out = []
        for i in s :
            if i == '(' :
                if stack :
                    out.append(i)
                stack += 1
            else :
                stack -= 1
                if stack :
                    out.append(i)
        return "".join(out)