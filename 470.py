# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True :
            no = (rand7() - 1) * 7 + rand7()
            if no <= 40 :
                return (no - 1) % 10 + 1