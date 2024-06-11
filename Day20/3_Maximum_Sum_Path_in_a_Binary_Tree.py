# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findMaxPathSum(root, maxi):
            if not root:
                return 0

            leftMaxPath = max(0, findMaxPathSum(root.left, maxi))
            rightMaxPath = max(0, findMaxPathSum(root.right, maxi))

            maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)

            return max(leftMaxPath, rightMaxPath) + root.val

        maxi = [float('-inf')]
        findMaxPathSum(root, maxi)
        return maxi[0]
