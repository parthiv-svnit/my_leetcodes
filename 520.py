class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n == 1 :
            return True
        if word[0].lower() == word[0] :
            for i in range(1, n) :
                if word[i].lower() != word[i] :
                    return False
            return True
        else :
            if word[1].lower() == word[1] :
                for i in range(2, n) :
                    if word[i].lower() != word[i] :
                        return False
                return True
            else :
                for i in range(2, n) :
                    if word[i].lower() == word[i] :
                        return False
                return True