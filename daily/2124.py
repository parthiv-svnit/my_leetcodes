class Solution:
    def checkString(self, s: str) -> bool:
        # print(sorted(s))
        return s == "".join(sorted(s))