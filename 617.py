# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2 :
            return root2
        def fun(node1, node2) :
            if not node1 :
                return
            if not node2 :
                return
            node1.val += node2.val
            if node1.left and node2.left :
                fun(node1.left, node2.left)
            if node2.right and node2.right :
                fun(node1.right, node2.right)
            
            if not node1.left and node2.left :
                node1.left = node2.left
            if not node1.right and node2.right :
                node1.right = node2.right
        fun(root1, root2)
        return root1