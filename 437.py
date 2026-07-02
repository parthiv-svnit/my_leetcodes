# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix = defaultdict(int)
        prefix[0] = 1

        def fun(node, csum) :
            if not node :
                return 0
            csum += node.val
            out = prefix[csum - targetSum]
            prefix[csum] += 1

            out += fun(node.left, csum)
            out += fun(node.right, csum)

            prefix[csum] -= 1
            return out
        return fun(root, 0)