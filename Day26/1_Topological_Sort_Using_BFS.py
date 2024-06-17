from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        topo = []
        indegree = [0] * V
        for vertex in range(V):
            for adjNode in adj[vertex]:
                indegree[adjNode] += 1
        
        q = deque()
        for vertex in range(V):
            if indegree[vertex] == 0:
                q.append(vertex)
                
        while q:
            node = q.popleft()
            topo.append(node)
            
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
                    
        return topo
