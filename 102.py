# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        arr = []
        def fun(node, d) :
            if not node :
                return
            if len(arr) == d :
                arr.append([])
            arr[d].append(node.val)
            fun(node.left, d + 1)
            fun(node.right, d + 1)
        
        fun(root, 0)
        return arr