# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        def dfs(root, depth):
            if root == None:
                return depth

            l = r = 0
            #if root.left:
            l = dfs(root.left, depth + 1)

            #if root.right:
            r = dfs(root.right, depth + 1)

            return max(l, r)

        return dfs(root, 0)
