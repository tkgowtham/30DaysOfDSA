class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist = [100000000] * V
        dist[S] = 0

        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        for u, v, wt in edges:
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist
