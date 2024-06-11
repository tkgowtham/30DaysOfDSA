'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def checkSum(node):
            if node is None or (node.left is None and node.right is None):
                return True
                
            child_sum = 0
            
            if node.left:
                child_sum += node.left.data
                
            if node.right:
                child_sum += node.right.data
                
            if node.data == child_sum:
                return checkSum(node.left) and checkSum(node.right)
            else:
                return False
        

        return 1 if checkSum(root) else 0
