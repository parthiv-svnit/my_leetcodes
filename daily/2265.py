# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        out = [0]
        def fun(node) :
            if not node :
                return 0, 0
            lsum, ln = fun(node.left)
            rsum, rn = fun(node.right)
            s = lsum + rsum + node.val
            n = ln + rn + 1
            if s // n == node.val :
                out[0] += 1
            return s, n
        fun(root)
        return out[0]