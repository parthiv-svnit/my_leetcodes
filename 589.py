"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def fun(node) :
            if not node :
                return
            arr.append(node.val)
            for i in node.children :
                fun(i)
        fun(root)
        return arr