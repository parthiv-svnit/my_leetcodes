# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderin = {val: inx for inx,val in enumerate(inorder)}

        prein = [0]

        def fun(l, r) :
            if l > r :
                return None
            rootval = preorder[prein[0]]
            root = TreeNode(rootval)
            prein[0] += 1

            rootin = inorderin[rootval]

            root.left = fun(l, rootin - 1)
            root.right = fun(rootin + 1, r)

            return root
        return fun(0, len(inorder) - 1)