# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def fun(node) :
            if not node :
                return None
            if p == node or q == node:
                return node
            l = fun(node.left)
            r = fun(node.right)
            if l and r :
                return node
            return l if l else r
        return fun(root)