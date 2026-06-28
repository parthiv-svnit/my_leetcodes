# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        out = [0]

        def fun(node) :
            if not node :
                return
            if node.left and not node.left.left and not node.left.right :
                out[0] += node.left.val
            fun(node.left)
            fun(node.right)
        fun(root)
        return out[0]