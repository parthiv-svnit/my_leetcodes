# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def fun(node) :
            if not node :
                return (0, 0)
            left_yes, left_no = fun(node.left)
            right_yes, right_no = fun(node.right)

            yes = node.val + left_no + right_no
            no = max(left_yes, left_no) + max(right_yes, right_no)

            return (yes, no)
        return max(fun(root))