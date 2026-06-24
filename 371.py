import ctypes
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c = 0
        while b != 0 :
            c = ctypes.c_int32((a & b) << 1).value
            a = ctypes.c_int32(a ^ b).value
            b = c
        return a