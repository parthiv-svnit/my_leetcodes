"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def fun(node) :
            if not node :
                return
            for i in node.children :
                fun(i)
            arr.append(node.val)
        fun(root)
        return arr