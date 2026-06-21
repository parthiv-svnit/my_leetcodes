class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)) :
            if s[i] in v :
                arr.append(i)
        
        i = 0
        j = len(arr) - 1
        s = list(s)
        while i < j :
            s[arr[i]], s[arr[j]] = s[arr[j]], s[arr[i]]
            i += 1
            j -= 1
        return ''.join(s)