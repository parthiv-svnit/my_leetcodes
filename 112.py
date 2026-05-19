# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root :
            return False

        def fun(node, v) :
            if not node :
                return False

            if not node.left and not node.right :
                return v + node.val == targetSum
                    
            return fun(node.left, v + node.val) or fun(node.right, v + node.val)

        return fun(root, 0)