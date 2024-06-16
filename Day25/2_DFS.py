class Solution:
    def dfs(self, node, adj, visited, ans):
        visited[node] = 1
        ans.append(node)
        
        for i in adj[node]:
            if visited[i] != 1:
                self.dfs(i, adj, visited, ans)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0] * V
        start = 0
        ans = []
        self.dfs(start, adj, visited, ans)
        return ans
