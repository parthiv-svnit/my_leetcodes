class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        out = 0
        for i in range(n) :
            if not visited[i] :
                curr = i
                count = 0
                while not visited[curr] :
                    visited[curr] = True
                    curr = nums[curr]
                    count += 1
                out = max(out, count)
        return out