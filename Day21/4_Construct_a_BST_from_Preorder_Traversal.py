# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildBST(preorder, lower, upper):
            nonlocal index
            if index == len(preorder):
                return None

            val = preorder[index]
            if val < lower or val > upper:
                return None
            
            index += 1
            root = TreeNode(val)
            root.left = buildBST(preorder, lower, val)
            root.right = buildBST(preorder, val, upper)
            return root

        index = 0
        return buildBST(preorder, float('-inf'), float('inf'))
