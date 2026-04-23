class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        i = 0

        while i <= len(s) - 1:
            if s[i] == 'M':
                out += 1000
            elif s[i] == 'D':
                out += 500
            elif s[i] == 'C' and i == len(s) - 1 :
                out += 100
                break
            elif s[i] == 'C':
                if s[i+1] == 'D':
                    out += 400
                    i+=1
                    
                elif s[i+1] == 'M':
                    out += 900
                    i+=1
                    
                else:
                    out += 100
                
            elif s[i] == 'L':
                out += 50
            elif s[i] == 'D':
                out += 500
            elif s[i] == 'X' and i == len(s) - 1 :
                out += 10
                break
            elif s[i] == 'X':
                if s[i+1] == 'L':
                    out += 40
                    i+=1
                    
                elif s[i+1] == 'C':
                    out += 90
                    i+=1
                    
                else:
                    out += 10
                
            elif s[i] == 'V':
                out += 5
            elif s[i] == 'I' and i == len(s) - 1 :
                out += 1
                break
            else:
                if s[i+1] == 'V':
                    out += 4
                    i+=1
                    
                elif s[i+1] == 'X':
                    out += 9
                    i+=1
                    
                else:
                    out += 1
            i+=1
        return out