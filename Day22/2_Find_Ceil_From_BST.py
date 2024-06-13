'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    ceil = float('inf')
    
    while root:
        if root.data == x:
            return root.data
        
        if root.data > x:
            ceil = root.data
            root = root.left
        else:
            root = root.right
    
    return ceil if ceil != float('inf') else -1
