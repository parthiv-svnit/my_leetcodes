# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def fun(node) :
            if not node :
                return
            arr.append(node.val)
            fun(node.left)
            fun(node.right)
        fun(root)
        arr = Counter(arr)
        arr = dict(sorted(arr.items(), key = lambda x : x[1], reverse = True))
        out = []
        count = 0
        for i, j in arr.items() :
            if not count :
                m1 = j
                count += 1
            if j != m1 :
                break
            out.append(i)
        return out