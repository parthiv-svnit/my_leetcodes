class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        csum = 0
        out = 0
        for num in nums :
            csum += num
            out += prefix[csum - k]
            prefix[csum] += 1
        return out