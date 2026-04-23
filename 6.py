class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        out = []
        if numRows == 1:
           return s
        
        for i in range(numRows):
            j=i
            while j < (len(s)):

                out.append(s[j])

                if i == 0 or i == numRows - 1:
                
                    j = j + 2*(numRows-1)
                else:
                
                    j = j + 2*(numRows-1) - 2*i

                    if j > (len(s)-1):
                        break

                    out.append(s[j])

                    j = j + 2*i

                    if j > (len(s)-1):
                        break
        return "".join(out)

a = Solution()
print(a.convert("PAYPALISHIRING",4))