class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        di = Counter(s)

        di = sorted(di.items(), key = lambda x : x[1], reverse = True)
        
        out = [x[0] * x[1] for x in di]
        return "".join(out)