# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseInorder(self, node, counter, k, kLarge):
        if node == None or counter[0] >= k:
            return

        self.reverseInorder(node.right, counter, k, kLarge)
        counter[0] += 1
        if counter[0] == k:
            kLarge[0] = node.val
            return

        self.reverseInorder(node.left, counter, k, kLarge)
      
    def inorder(self, node, counter, k, kSmall):
        if node == None or counter[0] >= k:
            return

        self.inorder(node.left, counter, k, kSmall)

        counter[0] += 1

        if counter[0] == k:
            kSmall[0] = node.val
            return

        self.inorder(node.right, counter, k, kSmall)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kSmall = [float('-inf')]
        #kLarge = [float('inf')]
        counter = [0]

        self.inorder(root, counter, k, kSmall)

        counter[0] = 0

        self.reverseInorder(root, counter, k, kLarge)

        return kSmall[0]
