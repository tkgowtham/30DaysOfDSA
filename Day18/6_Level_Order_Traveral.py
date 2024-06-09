# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        ans = []

        queue = [root]

        while queue:
            size = len(queue)

            level = []

            for i in range(size):
                node = queue.pop(0)

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
