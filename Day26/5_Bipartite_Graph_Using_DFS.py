class Solution:

    def dfs(obj, node, col, color, adj): #using obj instead self, just for demo purpose
        color[node] = col

        for adjNode in adj[node]:
            if color[adjNode] == -1:
                if obj.dfs(adjNode, 1 if col == 0 else 0, color, adj) == False:
                    return False
            elif color[adjNode] == col:
                return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if self.dfs(i, 0, color, graph) == False:
                    return False

        return True
