#import pickle
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
        def rserialize(node):
            if node is None:
                vals.append('null')
            else:
                vals.append(str(node.val))
                rserialize(node.left)
                rserialize(node.right)
        
        vals = []
        rserialize(root)
        return ','.join(vals)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize():
            if self.data[0] == 'null':
                self.data.pop(0)
                return None
            
            root = TreeNode(int(self.data.pop(0)))
            root.left = rdeserialize()
            root.right = rdeserialize()
            return root
        
        self.data = data.split(',')
        return rdeserialize()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
