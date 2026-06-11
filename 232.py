from collections import deque
class MyQueue(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1 :
            self.q2.append(self.q1.pop())
        x = self.q1.pop()
        while len(self.q2) > 0 :
            self.q1.append(self.q2.pop())
        return x

    def peek(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1 :
            self.q2.append(self.q1.pop())
        x = self.q1[-1]
        while len(self.q2) > 0 :
            self.q1.append(self.q2.pop())
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()