from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine) :
            return False
        di = Counter(magazine)

        for i in ransomNote :
            if i in di :
                di[i] -= 1
                if di[i] < 0 :
                    return False
            else :
                return False
        return True