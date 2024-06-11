# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def build(preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_map):
            if pre_start > pre_end or in_start > in_end:
                return None

            first_element_in_preorder = preorder[pre_start]
            root = TreeNode(val = first_element_in_preorder)

            inRoot = inorder_map[root.val]

            leftSubTreeSize = inRoot - in_start

            root.left = build(preorder, pre_start + 1, pre_start + leftSubTreeSize,
                             inorder, in_start, inRoot - 1,
                             inorder_map)

            root.right = build(preorder, pre_start + leftSubTreeSize + 1, pre_end,
                             inorder, inRoot + 1, in_end, 
                             inorder_map)

            return root

        root = build(preorder, 0, len(preorder) - 1,
                     inorder, 0, len(inorder) - 1,
                     inorder_map)

        return root
