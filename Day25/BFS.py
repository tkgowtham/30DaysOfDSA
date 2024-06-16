from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = [0]*V
        q = deque()
        visited[0] = 1
        q.append(0)
        
        bfs = []
        while q:
            node = q.popleft()
            bfs.append(node)
            for i in adj[node]:
                if visited[i] != 1:
                    visited[i] = 1
                    q.append(i)
        
        return bfs
