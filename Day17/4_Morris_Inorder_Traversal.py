# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(root, ans):
            if root == None:
                return []

            while root != None:
                if root.left == None:
                    ans.append(root.val)
                    root = root.right
                else:
                    prev = root.left
                    while prev.right != None and prev.right != root:
                        prev = prev.right

                    if prev.right == None:
                        prev.right = root
                        root = root.left
                    else:
                        prev.right = None
                        ans.append(root.val)
                        root = root.right

            return ans

        ans = traverse(root, ans)

        return ans
