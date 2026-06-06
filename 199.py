# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out = []
        def fun(node, d) :
            if not node :
                return
            if d == len(out) :
                out.append(node.val)
            fun(node.right, d + 1)
            fun(node.left, d + 1)
        fun(root, 0)
        return out