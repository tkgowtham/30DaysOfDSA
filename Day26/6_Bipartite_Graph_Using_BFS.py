from collections import deque
from typing import List

class Solution:

    def bfs(self, start: int, adj: List[List[int]], color: List[int]) -> bool:
        q = deque([start])
        color[start] = 0
        while q:
            node = q.popleft()
            for adjNode in adj[node]:
                if color[adjNode] == -1:
                    color[adjNode] = 1 - color[node]
                    q.append(adjNode)
                elif color[adjNode] == color[node]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if not self.bfs(i, graph, color): #This is to make sure every component the color is filled.
                    return False

        return True
