# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        temp = head
        temp1 = temp.next

        while temp.next and temp1.next :
            temp.next = temp.next.next
            temp1.next = head
            head = temp1
            temp1 = temp.next

        temp1.next = head
        head = temp1
        temp.next = None

        return head