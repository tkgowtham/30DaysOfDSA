# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Brute Force
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        leftH = self.getH(root.left)
        rightH = self.getH(root.right)

        if abs(leftH - rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False

    def getH(self, root):
        if root == None:
            return 0

        leftH = self.getH(root.left)
        rightH = self.getH(root.right)

        return max(leftH, rightH) + 1

# Optimised
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self.dfs(root) != -1

    def dfs(self, root):
        if root == None:
            return 0

        leftH = self.dfs(root.left)

        if leftH == -1:
            return -1

        rightH = self.dfs(root.right)

        if rightH == -1:
            return -1
        
        if abs(leftH - rightH) > 1:
            return  - 1

        return max(leftH, rightH) + 1
