# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        def height(node) :
            if not node :
                return 0
            return 1 + max(height(node.left), height(node.right))
        def fun(node, row, l, r) :
            if not node :
                return
            m = (l + r) // 2
            out[row][m] = str(node.val)
            fun(node.left, row + 1, l, m - 1)
            fun(node.right, row + 1, m + 1, r)
        h = height(root)
        out = [[""] * (2 ** h - 1) for i in range(h)]
        fun(root, 0, 0, 2 ** h - 2)
        return out