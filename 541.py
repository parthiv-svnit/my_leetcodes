class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        arr = [i for i in range(0, n, 2 * k)]
        print(arr)
        out = []
        n2 = len(arr)
        out.append(s[k - 1:: -1])
        for i in range(n2) :
            print(s[arr[i] + k - 1: arr[i] - 1: -1])
            out.append(s[arr[i] + k - 1: arr[i] - 1: -1])
            if i < n2 - 1 :
                out.append(s[arr[i] + k: arr[i + 1]])
        out.append(s[arr[i] + k: n])
        return ''.join(out)