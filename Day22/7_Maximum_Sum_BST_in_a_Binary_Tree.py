# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, minNode, maxNode, sumBST, isBST):
        self.minNode = minNode
        self.maxNode = maxNode
        self.sumBST = sumBST
        self.isBST = isBST

class Solution:
    def __init__(self):
        self.maxSum = 0

    def helper(self, root):
        if root is None:
            return Node(float('inf'), float('-inf'), 0, True)
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left.isBST and right.isBST and left.maxNode < root.val < right.minNode:
            currentSum = left.sumBST + root.val + right.sumBST
            self.maxSum = max(self.maxSum, currentSum)
            return Node(min(root.val, left.minNode), max(root.val, right.maxNode), currentSum, True)
        
        return Node(float('-inf'), float('inf'), 0, False)

    def maxSumBST(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maxSum 
