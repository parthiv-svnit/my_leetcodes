# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head :
            return None
        if not head.next :
            if head.val == val :
                return None
            else :
                return head
        temp = head
        
        while temp.val == val :
            if not temp.next :
                if temp.val == val :
                    return None
            temp = temp.next
            head = temp

        while temp and temp.next :
            if not temp.next.next :
                if temp.next.val == val :
                    temp.next = None
                    return head
            while temp.next is not None and temp.next.val == val :
                temp.next = temp.next.next
            temp = temp.next
           
        return head