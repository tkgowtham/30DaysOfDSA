# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        ans = 0
        queue = [[root, 0]]

        while queue:
            size = len(queue)
            mini = queue[-1][1]

            first = queue[0][1]
            last = 0

            for i in range(size):
                
                node, index = queue.pop(0)
                cur_id = index - first

                if i == size - 1:
                    last = cur_id

                if node.left:
                    queue.append([node.left, cur_id * 2 + 1])

                if node.right:
                    queue.append([node.right, cur_id * 2 + 2])

            ans = max(ans, last + 1)

        return ans
