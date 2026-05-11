# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head :
            return head 
            
        dummy = ListNode(0)
        curr = dummy

        curr.next = ListNode(head.val)
        curr = curr.next

        temp = head

        while temp.next :
            while temp.next and temp.val == temp.next.val :
                temp = temp.next
            if temp.next :
                temp = temp.next
                curr.next = ListNode(temp.val)
                curr = curr.next

        return dummy.next