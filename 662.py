# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        li = {}
        out = [0]
        def fun(node, level, index) :
            if not node :
                return
            if level not in li :
                li[level] = index
            out[0] = max(out[0], index - li[level] + 1)
            fun(node.left, level + 1, index * 2)
            fun(node.right, level + 1, index * 2 + 1)
        fun(root, 0, 0)
        return out[0]