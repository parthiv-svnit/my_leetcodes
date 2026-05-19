# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root :
            return root
        arr = []
        def fun(node) :
            if not node :
                return
            arr.append(node)
            fun(node.left)
            fun(node.right)
        fun(root) 
        
        for i in range(len(arr) - 1) :
            arr[i].left = None
            arr[i].right = arr[i + 1]

        arr[-1].left = None
        arr[-1].right = None