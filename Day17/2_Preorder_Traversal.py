# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        def traverse(root, ans):
            if root == None:
                return

            ans.append(root.val)

            traverse(root.left, ans)

            traverse(root.right, ans)

            return ans

        ans = traverse(root, ans)

        return ans
