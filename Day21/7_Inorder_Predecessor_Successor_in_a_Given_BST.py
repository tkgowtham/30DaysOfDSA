'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        def find_predecessor(node):
            if not node:
                return
            if node.key >= key:
                find_predecessor(node.left)
            else:
                pre.key = node.key
                find_predecessor(node.right)

        def find_successor(node):
            if not node:
                return
            if node.key <= key:
                find_successor(node.right)
            else:
                suc.key = node.key
                find_successor(node.left)

        find_predecessor(root)
        
        find_successor(root)
        
        return pre, suc
