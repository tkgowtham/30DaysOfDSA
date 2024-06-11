class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        def convert(root):
            if root == None:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            convert(root.left)
            convert(root.right)
            
        convert(root)
