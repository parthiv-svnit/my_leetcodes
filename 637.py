# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = []

        def fun(node, l) :
            if not node :
                return 
            if len(arr) == l :
                arr.append([])
            arr[l].append(node.val)
            fun(node.left, l + 1)
            fun(node.right, l + 1)
        fun(root, 0)
        print(arr)
        out = []
        for i in arr :
            out.append(sum(i) / len(i))
        return out