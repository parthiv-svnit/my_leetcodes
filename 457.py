class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        def nex(ind) :
            return (ind + nums[ind]) % n
        s = 0
        f = 0

        for i in range(n) :
            if nums[i] == 0 :
                continue
            s = i
            f = i
            sign = nums[i] > 0
            while (nums[s] > 0) == sign and (nums[f] > 0) == sign and (nums[nex(f)] > 0) == sign :
                s = nex(s)
                f = nex(nex(f))
                if s == f :
                    if s == nex(s) :
                        break
                    return True
            temp = i
            while nums[temp] != 0 and (nums[temp] > 0) == sign :
                temp1 = nex(temp)
                nums[temp] = 0
                temp = temp1
        return False