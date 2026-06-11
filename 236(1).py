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
            if p == node :
                return p
            elif q == node :
                return q
            l = fun(node.left)
            r = fun(node.right)
            if l is not None and r is not None :
                return node
            elif l is not None :
                return l
            return r
        return fun(root)