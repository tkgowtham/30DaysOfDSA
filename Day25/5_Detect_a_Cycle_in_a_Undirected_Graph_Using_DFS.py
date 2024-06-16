class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self, node, parent, visited, adj):
        visited[node] = 1
        for i in adj[node]:
            if visited[i] == 0:
                if self.dfs(i, node, visited, adj):
                    return True
            elif i != parent:
                return True
        
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = [0] * V
        for i in range(V):
            if visited[i] != 1:
                if self.dfs(i, -1, visited, adj):
                    return True
                    
        return False
