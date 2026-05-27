# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head :
            return None
        temp = head
        temp1 = []
        i = 0
        while temp.next :
            temp1.append(temp)
            temp = temp.next
            i += 1
        temp1.append(temp)
        j = 0
        while j < i :
            temp1[j].next = temp1[i]
            j += 1
            if i == j :
                break
            temp1[i].next = temp1[j]
            i -= 1
        temp1[j].next = None