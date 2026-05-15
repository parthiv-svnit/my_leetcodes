# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def fun(node, l = -float('inf'), h = float('inf')) :
            if not node :
                return True
            if not (l < node.val < h) :
                return False
            return (fun(node.left, l, node.val)) and (fun(node.right, node.val, h))
        return fun(root)