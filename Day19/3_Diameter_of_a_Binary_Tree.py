# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def hieght(root):
            if root == None:
                return 0

            l = hieght(root.left)
            r = hieght(root.right)

            self.diameter = max(self.diameter, l + r)

            return max(l, r) + 1

        hieght(root)
        return self.diameter
