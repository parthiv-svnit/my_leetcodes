class Solution:
    def judgeCircle(self, moves: str) -> bool:
        di = Counter(moves)
        outx = di['R'] - di['L']
        outy = di['U'] - di['D']

        if outx or outy :
            return False
        return True