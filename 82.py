# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        arr = []

        while temp != None :
            if temp.val not in arr :
                arr.append(temp.val)
            else :
                
                while temp.next is not None and temp.next.val == temp.val :
                    temp = temp.next
                if temp.next is None :
                    arr.pop()
                    break
                arr.pop()
                
            temp = temp.next
        
        ll = ListNode(0)
        curr = ll

        for val in arr :
            curr.next = ListNode(val)
            curr = curr.next

        return ll.next