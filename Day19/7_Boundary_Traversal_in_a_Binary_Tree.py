'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right
    
    def addLeftBoundary(self, root, res):
        cur = root.left
        while cur:
            if not self.isLeaf(cur):
                res.append(cur.data)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
                
                
    def addRightBoundary(self, root, res):
        cur = root.right
        temp = []
        while cur:
            if not self.isLeaf(cur):
                temp.append(cur.data)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
                
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])
            
    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        
        if root.left:
            self.addLeaves(root.left, res)
            
        if root.right:
            self.addLeaves(root.right, res)
            
    def printBoundaryView(self, root):
        # Code here
        if root == None:
            return []
            
        res = []
        if not self.isLeaf(root):
            res.append(root.data)
            
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)
        
        return res
