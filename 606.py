# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def fun(node) :
            if not node :
                return
            if not node.left and not node.right :
                return f"{node.val}"
            if not node.left :
                return f"{node.val}()({fun(node.right)})"
            if not node.right :
                return f"{node.val}({fun(node.left)})"
            return f"{node.val}({fun(node.left)})({fun(node.right)})"
        return fun(root)