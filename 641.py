class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * (self.k)
        self.head = -1
        self.tail = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1) % self.k

        self.queue[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k

        self.queue[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.k

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.k == self.head


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()