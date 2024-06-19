import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        queue = []
        visited = [0] * V
        heapq.heappush(queue, (0,0))
        sums = 0
        while queue:
            wt, node = heapq.heappop(queue)
            if visited[node] == 1:
                continue
            visited[node] = 1
            sums += wt
            for adjNode in adj[node]:
                aNode, awt = adjNode
                if not visited[aNode]:
                    heapq.heappush(queue, (awt, aNode))
                    
        
        return sums
