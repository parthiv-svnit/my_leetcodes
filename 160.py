# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ta = headA
        tb = headB

        while ta != tb :
            if ta is None :
                ta = headB 
            else :
                ta = ta.next
            if tb is None :
                tb = headA
            else :
                tb = tb.next
        return ta