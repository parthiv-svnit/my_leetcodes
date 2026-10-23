class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i+1] for i in range(len(s) - 1)):
            return 0
        if len(s) == 2 :
            return -1
        arr = []
        for i in s :
            arr.append(ord(i) - 97)
        # print(arr)
        mmin = min(arr)
        mmax = max(arr)
        n = len(s)
        # i = 0
        # out = 0
        # while i < n - 1 :
        #     j = i + 1
        #     while j < n and arr[j] < arr[i] :
        #         if j == i + 1 :
        #             if i == 0 and j == n - 1 :
        #                 return -1
        #             out += 1
        #         j += 1
        #     i += 1
        # return out
        if arr[0] == mmin or arr[n - 1] == mmax:
            return 1
        for i in range(1, n - 1):
            if arr[i] == mmin or arr[i] == mmax:
                return 2
        return 3