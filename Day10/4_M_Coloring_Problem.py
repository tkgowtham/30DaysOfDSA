#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
#TC = O(N^M) SC=O(N)
def graphColoring(graph, m, V):
    
    #your code here
    def isSafe(node, graph, color, col):
        for i in range(V):
            if graph[node][i] == 1 and color[i] == col:
                return False
                
        return True
    
    def solve(node, graph, color, m, V):
        if node == V:
            return True
            
        for col in range(1,m+1):
            if isSafe(node, graph, color, col):
                color[node] = col
                if solve(node + 1, graph, color, m, V) == True:
                    return True
                color[node] = 0
        
        return False
    
    color = [0] * V
    if solve(0, graph, color, m, V):
        return 1
    else:
        return 0
