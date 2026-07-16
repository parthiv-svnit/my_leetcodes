# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        out = []
    
        def fun(node, level) :
            if not node :
                return
            if len(out) == level :
                out.append(node.val)
            out[level] = max(out[level], node.val)
            fun(node.left, level + 1)
            fun(node.right, level + 1)
        fun(root, 0)
        return out