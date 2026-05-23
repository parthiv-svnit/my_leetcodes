# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        out = [0]
        arr = []
        def fun(node, arr) :
            if not node :
                return
            arr.append(node.val)
            if not node.left and not node.right :
                no = int("".join(map(str, arr)))
                out[0] += no
            fun(node.left, arr)
            fun(node.right, arr)
            arr.pop()
            
        fun(root, arr)
        return out[0]