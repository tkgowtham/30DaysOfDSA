'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        self.prev = None
        self.head = None
        
    def bToDLL(self,root):
        # do Code here
        if root == None:
            return None
        
        self.bToDLL(root.left)
        
        if self.prev == None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
            
        self.prev = root
        
        self.bToDLL(root.right)
        
        return self.head
