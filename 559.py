"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        out = [0]
        def fun(node, d) :
            if not node :
                return
            if not node.children :
                out[0] = max(out[0], d)
            for n in node.children :
                fun(n, d + 1)
            
        fun(root, 1)
        return out[0]