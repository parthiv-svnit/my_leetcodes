class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        deca = int(a,2)
        decb = int(b,2)

        decout = deca + decb

        return bin(decout)[2:]