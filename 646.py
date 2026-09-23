class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        print(pairs)
        lsp = pairs[0][1]
        out = 1
        for i, j in pairs :
            if i > lsp :
                out += 1
                lsp = j
        return out