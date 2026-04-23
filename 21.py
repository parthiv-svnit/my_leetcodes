# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1, l2 = list1, list2
        list = ListNode(0)
        temp = list

        while l1 and l2 :
            if l1.val <= l2.val :
                temp.next = l1
                l1 = l1.next
                
            else :
                temp.next = l2
                l2 = l2.next

            temp = temp.next
                
        if l1 :
            temp.next = l1
        elif l2 :
            temp.next = l2

        return list.next
