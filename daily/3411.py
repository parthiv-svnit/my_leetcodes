class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        out = 0
        def lcm(a, b):
            return (a * b) // math.gcd(a, b)
        
        total_lcm = 1
        max_val = max(nums)
        for x in nums:
            total_lcm = lcm(total_lcm, x)
        max_p = total_lcm * max_val

        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = math.gcd(g, nums[j])
                l = lcm(l, nums[j])
                
                if p == g * l:
                    out = max(out, j - i + 1)
                
                if p > max_p:
                    break
                    
        return out