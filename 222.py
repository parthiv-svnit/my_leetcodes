# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        out = [0]
        def fun(node) :
            if not node :
                return
            out[0] += 1
            fun(node.left)
            fun(node.right)
        fun(root)
        return out[0]