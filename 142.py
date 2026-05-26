# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return None
        temp = head

        while temp.next :
            if temp.val is '.' :
                return temp
            temp.val = '.'
            temp = temp.next
        if temp.next is not None :
            return temp.next
        return None