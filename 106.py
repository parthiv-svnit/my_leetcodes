# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderin = {val: inx for inx,val in enumerate(inorder)}

        prein = [len(postorder) - 1]

        def fun(l, r) :
            if l > r :
                return None
            rootval = postorder[prein[0]]
            root = TreeNode(rootval)
            prein[0] -= 1

            rootin = inorderin[rootval]

            root.right = fun(rootin + 1, r)
            root.left = fun(l, rootin - 1)

            return root
        return fun(0, len(inorder) - 1)