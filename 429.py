"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root :
            return []
        
        out = []

        def fun(node, level) :
            if not node :
                return
            if len(out) == level :
                out.append([])
            out[level].append(node.val)

            for n in node.children :
                fun(n, level + 1)

        fun(root, 0)

        return out