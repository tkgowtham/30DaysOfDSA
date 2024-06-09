"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        if root == None:
            return []
        
        def dfs(root, path, res):
            if root == None:
                return
                
            path.append(root.data)
            
            if not root.left and not root.right:
                res.append(list(path))
            else:
                if root.left:
                    dfs(root.left, path, res)
                if root.right:
                    dfs(root.right, path, res)
            
            path.pop()
            
        ans = []
        dfs(root, [], ans)
        
        return ans
