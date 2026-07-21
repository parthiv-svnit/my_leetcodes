# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return root
        arr = []
        def fun(node) :
            if not node :
                return
            arr.append(node.val)
            fun(node.left)
            fun(node.right)
        fun(root)
        print(arr)
        arr.sort(reverse = True)
        di = {}
        di[arr[0]] = arr[0]
        x = 0
        for i in range(1, len(arr)) :
            x = arr[i]
            arr[i] += arr[i - 1]
            di[x] = arr[i]
        def fun2(node) :
            if not node :
                return 
            node.val = di[node.val]
            fun2(node.left)
            fun2(node.right)
        fun2(root)
        return root