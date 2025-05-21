# link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
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

        serial_list = []

        def traverse(node):
            if node is None:
                serial_list.append("N")
                return
            serial_list.append(f"{node.val}")
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ",".join(serial_list)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data.split(",")
        self.idx = 0
        n = len(self.data)
        def traverse():
            if self.data[self.idx] == "N":
                return None
            node = TreeNode(int(self.data[self.idx]))
            self.idx += 1
            if self.idx < n:
                node.left = traverse()
                self.idx += 1
            if self.idx < n:
                node.right = traverse()

            return node
        
        return traverse()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

