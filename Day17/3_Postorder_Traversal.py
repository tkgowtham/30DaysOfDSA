# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def traverse(root, ans):
            if root == None:
                return

            traverse(root.left, ans)

            traverse(root.right, ans)

            ans.append(root.val)

            return ans

        ans = traverse(root, ans)

        return ans
