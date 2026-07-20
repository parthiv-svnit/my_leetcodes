# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def fun(node) :
            if not node :
                return 
            arr.append(node.val)
            fun(node.left)
            fun(node.right)
        fun(root)
        arr.sort()
        out = float('inf')
        for i in range(len(arr) - 1) :
            out = min(out, abs(arr[i] - arr[i + 1]))
        return out