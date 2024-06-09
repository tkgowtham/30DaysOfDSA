# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        map = {}
        queue = [[root, 0, 0]]

        while queue:
            node, vertical, horizontal = queue.pop(0)

            if vertical in map:
                map[vertical].append([horizontal, node.val])
            else:
                map[vertical] = [[horizontal, node.val]]

            if node.left:
                queue.append([node.left, vertical - 1, horizontal + 1])
            
            if node.right:
                queue.append([node.right, vertical + 1, horizontal + 1])

        ans = []

        for vertical in sorted(map.keys()):
            level = sorted(map[vertical])
            #print(level)
            ans.append([val for horizontal, val in level])

        return ans
