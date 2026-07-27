class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = float('-inf')
        m2 = float('-inf')
        
        for i in nums :
            if i > m1 :
                m2 = m1
                m1 = i
            elif i > m2 :
                m2 = i
        return (m1 - 1) * (m2 - 1)