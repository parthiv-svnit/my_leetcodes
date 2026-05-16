# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root :
            return 0
        m = [0]
        def fun(node, l) :
            if not node :
                return
            m[0] = max(m[0], l)
            
            fun(node.left, l + 1)
            fun(node.right, l + 1)

        fun(root, 1)
        return m[0]