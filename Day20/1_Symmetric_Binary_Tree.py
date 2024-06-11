class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None:
            return False

        return root.left == root.right and self.isSymmetric(root.left) and self.isSymmetric(root.right)
