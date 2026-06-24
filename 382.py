# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        temp = self.head
        self.count = 0
        while temp :
            temp = temp.next
            self.count += 1

    def getRandom(self):
        """
        :rtype: int
        """
        tempc = random.randint(1, self.count)
        count1 = 1
        self.temp = self.head
        while count1 != tempc :
            self.temp = self.temp.next
            count1 += 1
        return self.temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()