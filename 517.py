class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines) % n != 0 :
            return -1
        target = sum(machines) // n
        diff = 0
        balance = 0
        out = 0
        for i in machines :
            diff = i - target
            balance += diff
            out = max(out, diff, abs(balance))
        return out