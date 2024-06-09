# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        if root == None:
            return []
        
        map = {}
        queue = [[root,0]]
        
        while queue:
            node, line = queue.pop(0)
            
            if line not in map:
                map[line] = node.data
                
            if node.left:
                queue.append([node.left, line - 1])
                
            if node.right:
                queue.append([node.right, line + 1])
                
        ans = []
        for i in sorted(map):
            ans.append(map[i])
            
        return ans
