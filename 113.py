# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        out = []
        if not root :
            return out
        def fun(node, currarr, remainsum) :
            if not node :
                return
            currarr.append(node.val)
            if not node.left and not node.right and remainsum == node.val :
                out.append(list(currarr))
            else :
                fun(node.left, currarr, remainsum - node.val)
                fun(node.right, currarr, remainsum - node.val)
            currarr.pop()
        fun(root, [], targetSum)
        return out