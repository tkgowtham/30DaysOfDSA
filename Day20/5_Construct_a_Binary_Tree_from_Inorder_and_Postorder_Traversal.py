# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == None or postorder == None or len(inorder) != len(postorder):
            return None

        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def build(postorder, post_start, post_end, inorder, in_start, in_end, inorder_map):
            if post_start > post_end or in_start > in_end:
                return None

            first_element_in_postorder = postorder[post_end]
            root = TreeNode(val = first_element_in_postorder)

            inRoot = inorder_map[root.val]

            leftSubTreeSize = inRoot - in_start

            root.left = build(postorder, post_start, post_start + leftSubTreeSize - 1,
                             inorder, in_start, inRoot - 1,
                             inorder_map)

            root.right = build(postorder, post_start + leftSubTreeSize, post_end - 1,
                             inorder, inRoot + 1, in_end, 
                             inorder_map)

            return root

        root = build(postorder, 0, len(postorder) - 1,
                     inorder, 0, len(inorder) - 1,
                     inorder_map)

        return root
