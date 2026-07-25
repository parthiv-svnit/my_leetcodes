# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        out = [0]
        def fun(node) :
            if not node :
                return 0
            l = fun(node.left)
            r = fun(node.right)
            out[0] += abs(r - l)
            return l + r + node.val
        fun(root)
        return out[0]