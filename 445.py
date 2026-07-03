# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1.next and l1.val == 0 :
            return l2
        if not l2.next and l2.val == 0 :
            return l1
        s1 = []
        s2 = []
        temp = l1
        while temp :
            s1.append(temp.val)
            temp = temp.next
        temp = l2
        while temp :
            s2.append(temp.val)
            temp = temp.next

        s1 = int(''.join(map(str, s1)))
        s2 = int(''.join(map(str, s2)))
        out = s1 + s2
        out = list(map(int, str(out)))

        if s1 < s2 :
            l1, l2 = l2, l1
            s1, s2 = s2, s1
        temp = l1
        head = temp
        i = 0
        while temp.next :
            temp.val = out[i]
            temp = temp.next
            i += 1
        temp.val = out[i]
        if len(str(s1)) != len(out) :
            i += 1
            temp.next = ListNode(out[i])

        return head