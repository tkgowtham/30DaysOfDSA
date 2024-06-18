from collections import deque
class Solution:
    
    def dfs(self, node, visited, adj, stack):
        visited[node] = 1
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, adj, stack)
                
        stack.append(node)
        
    def dfs2(self, node, visited, adj):
        visited[node] = 1
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs2(adjNode, visited, adj)
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        visited = [0] * V
        stack = deque()
        for i in range(V):
            if not visited[i]:
                self.dfs(i, visited, adj, stack)
                
                
        adjT = [[] for i in range(V)]
        for i in range(V):
            for adjNode in adj[i]:
                adjT[adjNode].append(i)
         
        visited = [0] * V
        scc = 0       
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc += 1
                self.dfs2(node, visited, adjT)
        
        return scc
