# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        even = []
        odd = []
        turn = 0
        while temp :
            if turn == 1 :
                odd.append(temp.val)
                turn = 0
            else :
                even.append(temp.val)
                turn = 1
            temp = temp.next
        temp = head
        turn = 0
        i = 0
        n = len(even)
        while temp and i < n :
            temp.val = even[i]
            i += 1
            temp = temp.next
        i = 0
        n = len(odd)
        while temp and i < n :
            temp.val = odd[i]
            i += 1
            temp = temp.next
        return head