"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head :
            return head
        temp = head
        temp1 = temp.next
        
        def fun(node) :
            temp = node
            tail = node
            while temp :
                temp1 = temp.next
                tail = temp
                if temp.child :
                    tail = fun(temp.child)
                    temp.next = temp.child
                    temp.child = None
                    temp.next.prev = temp
                    tail.next = temp1
                    if temp1 :
                        temp1.prev = tail
                
                temp = temp1
            return tail
        fun(head)
        return head