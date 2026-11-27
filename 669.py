# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        def fun(node) :
            if not node :
                return
            if node.val < low :
                return fun(node.right)
            elif node.val > high :
                return fun(node.left)

            node.left = fun(node.left)
            node.right = fun(node.right)

            return node
        return fun(root)