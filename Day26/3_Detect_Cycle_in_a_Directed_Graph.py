class Solution:
    
    def dfs(self, vertex, adj, visited):
        visited[vertex] -= 1
        for adjNode in adj[vertex]:
            if visited[adjNode] == -1:
                return True
            if visited[adjNode] == 0:
                if self.dfs(adjNode, adj, visited):
                    return True
                
        visited[vertex] = 1
        return False
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        visited = [0] * V
        for vertex in range(V):
            if visited[vertex] == 0:
               if self.dfs(vertex, adj, visited):
                   return True
            
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        return self.topoSort(V, adj)
