# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        def fun(node) :
            if not node :
                return None
            if not node.next :
                return TreeNode(node.val)
            p = None
            l, r  = node, node
            while r and r.next :
                p = l
                l = l.next
                r = r.next.next
            if p :
                p.next = None
            root = TreeNode(l.val)
            root.left = fun(node)
            root.right = fun(l.next)

            return root
        return fun(head)