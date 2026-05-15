# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root :
            return True
        def fun(p ,q) :
            if not p and not q :
                return True
            elif (not p or not q) or p.val != q.val :
                return False
            return fun(p.left, q.right) and fun(p.right, q.left)
        
        return fun(root.left, root.right)