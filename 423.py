from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        d = [0] * 10
        d[0] = count['z']
        d[2] = count['w']
        d[4] = count['u']
        d[6] = count['x']
        d[8] = count['g']

        d[3] = count['h'] - d[8]
        d[5] = count['f'] - d[4]
        d[7] = count['s'] - d[6]

        d[1] = count['o'] - d[0] - d[2] - d[4]
        d[9] = count['i'] - d[5] - d[6] - d[8]

        out = ''
        for i in range(10) :
            if d[i] :
                out += d[i] * str(i)
        return out