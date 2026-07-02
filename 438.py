class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        ls = len(s)
        if ls < lp :
            return []
        
        arr = Counter(s[:lp])
        di = Counter(p)
        out = []
        
        if arr == di :
            out.append(0)

        for i in range(1, ls - lp + 1) :
            arr[s[i - 1]] -= 1
            if arr[s[i - 1]] == 0 :
                del arr[s[i - 1]]
            arr[s[i + lp - 1]] += 1

            if arr == di :
                out.append(i)

        return out