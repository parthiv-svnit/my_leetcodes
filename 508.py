# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def fun(node) :
            if not node :
                return 0
            l = fun(node.left)
            r = fun(node.right)
            x = node.val + l + r
            out.append(x)
            return x

        fun(root)
        di = Counter(out)
        di = sorted(di.items(), key = lambda x : x[1], reverse = True)
        xval = di[0][1]
        if xval == 1 :
            return out
        out1 = []
        
        for x, y in di :
            if y == xval :
                out1.append(x)
            else :
                break
        return out1