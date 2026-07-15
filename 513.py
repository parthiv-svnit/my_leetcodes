# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        out = [[0, -1]]
        def fun(node, level) :
            if not node :
                return 
            if not node.left and not node.right :
                if level > out[0][1] :
                    out[0] = [node.val, level]
            fun(node.left, level + 1)
            fun(node.right, level + 1)
        fun(root, 0)
        return out[0][0]