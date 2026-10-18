class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i in range(n) :
            temp = nums[i]
            x = 0
            while temp :
                x += temp % 10
                temp //= 10
            arr.append((x, nums[i], i))
        arr.sort()
        # print(arr)
        visit = [False] * n
        out = 0

        for i in range(n) :
            if visit[i] :
                continue
            j = i
            clen = 0
            while not visit[j] :
                visit[j] = True
                clen += 1
                j = arr[j][2]
            if clen > 1 :
                out += clen - 1
        return out