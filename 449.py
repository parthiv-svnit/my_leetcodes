# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []
        def fun(node) :
            if not node :
                return
            out.append(node.val)
            fun(node.left)
            fun(node.right)
        fun(root)
        return ",".join(map(str, out))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data :
            return None
        out = list(map(int, data.split(',')))
        self.i = 0

        def fun(l, r) :
            if self.i == len(out) :
                return None
            val = out[self.i]
            if val <= l or val >= r :
                return None
            self.i += 1
            node = TreeNode(val)
            node.left = fun(l, val)
            node.right = fun(val, r)

            return node
        return fun(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans