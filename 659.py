class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        di = Counter(nums)
        tail = Counter()

        for i in nums :
            if not di[i] :
                continue
            if tail[i - 1] > 0 :
                tail[i - 1] -= 1
                tail[i] += 1
                di[i] -= 1
            elif di[i + 1] > 0 and di[i + 2] > 0 :
                di[i + 1] -= 1
                di[i + 2] -= 1
                tail[i + 2] += 1
                di[i] -= 1
            else :
                return False
        return True