class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum :
            return ""
        out = []
        for i in range(num) :
            if sum >= 9 :
                out.append(9)
                sum -= 9
            
            elif sum == 0 :
                out.append(0)
                
            else :
                out.append(sum)
                sum -= sum
        return "".join(map(str, out))