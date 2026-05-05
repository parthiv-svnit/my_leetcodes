# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0 :
            return head
        temp = head
        n = 0
        k1 = k
        while temp :
            temp = temp.next
            n += 1
        temp = head

        k = k % n
        while k > 0 :
            temp = head
            while temp.next and temp.next.next :
                temp = temp.next
            temp1 = temp.next
            temp1.next = head
            temp. next = None
            head = temp1
            k -= 1

        return head