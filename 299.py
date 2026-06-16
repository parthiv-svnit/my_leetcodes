from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        s = []
        g = []
        for i,j in zip(secret, guess) :
            if j == i :
                bull += 1
            else :
                s.append(i)
                g.append(j)
        cow = sum((Counter(s) & Counter(g)).values())
        return str(bull) + "A" + str(cow) + "B"