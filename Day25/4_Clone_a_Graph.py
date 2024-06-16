# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        maps = {}
        q = deque()
        src = node
        q.append(src)
        node = None
        node = UndirectedGraphNode(0)
        node.label = src.label
        maps[src] = node
        
        while q:
            u = q.popleft()
            v = u.neighbors
            for neighbor in v:
                if neighbor not in maps:
                    node = UndirectedGraphNode(neighbor.label)
                    maps[neighbor] = node
                    q.append(neighbor)
                maps[u].neighbors.append(maps[neighbor])
        
        return maps[src]
