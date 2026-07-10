class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3 :
            return 1
        magic = [1, 2, 2]
        head = 2
        num = 1
        out = 1
        while len(magic) < n :
            count = magic[head]
            for _ in range(count) :
                if len(magic) == n :
                    break
                magic.append(num)
                if num == 1 :
                    out += 1
            num = 2 if num == 1 else 1
            head += 1
        return out