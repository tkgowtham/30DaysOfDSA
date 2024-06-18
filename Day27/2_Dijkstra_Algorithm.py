import heapq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = []
        dist = [float('inf')] * V
        parent = [-1] * V
        
        dist[S] = 0
        heapq.heappush(pq, (0, S))
        
        while pq:
            dis, node = heapq.heappop(pq)
            for neighbor in adj[node]:
                adjNode, weight = neighbor
                if dist[node] + weight < dist[adjNode]:
                    dist[adjNode] = dist[node] + weight
                    parent[adjNode] = node
                    heapq.heappush(pq, (dist[adjNode], adjNode))
                    

        return dist
