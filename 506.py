class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        di = {}
        temp = 1
        for i in sorted(score, reverse = True) :
            di[i] = temp
            temp += 1
        out = []
        for i in score :
            if di[i] == 1 :
                out.append("Gold Medal")
            elif di[i] == 2 :
                out.append("Silver Medal")
            elif di[i] == 3 :
                out.append("Bronze Medal")
            else :
                out.append(str(di[i]))
        return out