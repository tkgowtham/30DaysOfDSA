from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def detect(self, src, adj, visited):
        visited[src] = 1
        queue = deque()
        queue.append((src, -1))
        
        while queue:
            node, parent = queue.popleft()
            for i in adj[node]:
                if visited[i] != 1:
                    visited[i] = 1
                    queue.append((i, node))
                elif parent != i:
                    return True
                    
        
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = [0] * V
        for i in range(V):
            if visited[i] != 1:
                if self.detect(i, adj, visited):
                    return True
                    
        return False
