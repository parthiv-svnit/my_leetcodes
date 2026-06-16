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
        def fun(nodes) :
            if not nodes :
                return
            nxt = []

            for node in nodes :
                if node :
                    out.append(str(node.val))
                    nxt.append(node.left)
                    nxt.append(node.right)
                else :
                    out.append("null")
            fun(nxt)
        fun([root])
        return ",".join(out)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "null" :
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1

        while queue and i < len(nodes) :
            node = queue.pop(0)

            if nodes[i] != 'null' :
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(nodes) and nodes[i] != "null" :
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))