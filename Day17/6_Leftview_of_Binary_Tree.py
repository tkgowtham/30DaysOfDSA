'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    ans = []
    
    def leftRecursion(root, level, ans):
        if root == None:
            return
        
        if len(ans) == level:
            ans.append(root.data)
            
        leftRecursion(root.left, level + 1, ans)
        
        leftRecursion(root.right, level + 1, ans)
        
        
    leftRecursion(root, 0, ans)
    
    return ans
