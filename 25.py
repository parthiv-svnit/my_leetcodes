# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        current = head

        out = ListNode(0)
        final = out

        while current :

            count1 = 1

            while count1 < k :

                if count1 == 1 :
                    temp = ListNode(current.val)
                    current = current.next
                    if current.next is None :   
                        break
                    count1 += 1
                    continue

                new = ListNode(current.val)
                new.next = temp
                temp = new
                current = current.next
                count1 += 1
            
            

            while final.next :
                final = final.next

            while temp :
                final.next = temp
                temp = temp.next

        return out.next

a = Solution()
head = ListNode(1)
l1 = ListNode(2)
l1.next = head
l2 = ListNode(3)
l2.next = l1
l3 = ListNode(4)
l3.next = l2
print(a.reverseKGroup(head, 2))