from collections import deque
class Solution:
    
    def dfs(self, vertex, adj, visited, stack):
        visited[vertex] = 1
        for adjNode in adj[vertex]:
            if visited[adjNode] != 1:
                self.dfs(adjNode, adj, visited, stack)
                
        stack.append(vertex)
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        topo = []
        indegree = [0] * V
        
        for vertex in range(V):
            for adjNode in adj[vertex]:
                indegree[adjNode] += 1
        
        stack = deque()
        visited = [0] * V
        for vertex in range(V):
            if indegree[vertex] == 0:
                self.dfs(vertex, adj, visited, stack)
                    
                    
        while stack:
            topo.append(stack.pop())

        return topo
