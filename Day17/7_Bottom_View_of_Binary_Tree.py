from collections import deque

class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return []

        ans = []
        hd_node_map = {}
        queue = deque([[root, 0]])

        while queue:
            node, hd = queue.popleft()
            hd_node_map[hd] = node.data

            if node.left:
                queue.append([node.left, hd - 1])
                
            if node.right:
                queue.append([node.right, hd + 1])

        for key in sorted(hd_node_map):
            ans.append(hd_node_map[key])

        return ans
