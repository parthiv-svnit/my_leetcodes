"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head :
            return None
        if not head.next :
            Head = Node(head.val)
            if head.random != None :
                Head.random = Head
            return Head
        temp = head
        Head = Node(temp.val)
        temp2 = Head
        temp = temp.next

        while temp.next :
            temp2.next = Node(temp.val)
            temp2 = temp2.next
            temp = temp.next
        temp2.next = Node(temp.val)
        
        temp = head
        temp2 = Head
        while temp :
            temp1 = head
            temp21 = Head
            while temp1.next and temp1 != temp.random :
                temp1 = temp1.next
                temp21 = temp21.next
            if temp1 == temp.random :
                temp2.random = temp21
            else :
                temp2.random = None
            temp = temp.next
            temp2 = temp2.next
        return Head