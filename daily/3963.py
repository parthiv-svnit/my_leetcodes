class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        out = ["." * n]
        for i in range(1, m) :
            out.append("#" * (n - 1) + ".")
        return out