class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        root_u = self.findUPar(u)
        root_v = self.findUPar(v)
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

    def unionBySize(self, u, v):
        root_u = self.findUPar(u)
        root_v = self.findUPar(v)
        if root_u == root_v:
            return
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        
        
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        edges = []
        for node in range(V):
            for adjNode in adj[node]:
                aNode, awt = adjNode
                edges.append((awt, (node, aNode)))
                
                
        edges.sort()
        sums = 0
        ds = DisjointSet(V)
        for i in edges:
            wt = i[0]
            u, v = i[1]
            if ds.findUPar(u) != ds.findUPar(v):
                sums += wt
                ds.unionBySize(u,v);
                    
        
        return sums
