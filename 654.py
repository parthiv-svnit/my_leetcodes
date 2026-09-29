# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def fun(nums) :
            if not nums :
                return None
            nv = max(nums)
            nvi = nums.index(nv)
            node = TreeNode(nv, fun(nums[: nvi]), fun(nums[nvi + 1 :]))
            return node
        root = fun(nums)
        return root