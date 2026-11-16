class Solution:
    def digitSum(self, s: str, k: int) -> str:
        out = s
        while len(out) > k :
            temp = ""
            i = 0
            while i < len(out) :
                temp += str(sum(list(map(int, out[i: i + k]))))
                # print(str(sum(list(map(int, s[i: i + k])))), s[i: i + k])
                i += k
            out = temp
        return out