#Using toposort and Kahn's algorithm
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        indegree = [0] * V
        for node in range(V):
            for adjNode in adj[node]:
                indegree[adjNode] += 1
        
        q = deque()
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
                    
        
        if count == V:
            return False
        else:
            return True
