class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m = len(img)
        n = len(img[0])

        out = [[0] * n for _ in range(m)]

        for i in range(m) :
            for j in range(n) :
                total = 0
                no = 0

                for di in range(-1, 2) :
                    for dj in range(-1, 2) :
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < m and 0 <= nj < n :
                            total += img[ni][nj]
                            no += 1

                out[i][j] = total // no

        return out