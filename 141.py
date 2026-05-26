# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head :
            return False
        temp = head
        while temp.next :
            if temp.val == '.' :
                return True
            temp.val = '.'
            temp = temp.next
        if temp.next is not None :
            return True
        return False