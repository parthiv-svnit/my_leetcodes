# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root :
            return 0
        
        def fun(node) :
            if not node.left and not node.right :
                return 1
            if not node.left :
                return 1 + fun(node.right)
            if not node.right :
                return 1 + fun(node.left)

            return 1 + min(fun(node.left), fun(node.right))
        
        return fun(root)