from typing import List, Tuple

class Solution:
    def dfs(self, row: int, col: int, visited: List[List[bool]], grid: List[List[str]], vec: List[Tuple[int, int]], row0: int, col0: int) -> None:
        visited[row][col] = True
        vec.append((row - row0, col - col0))
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for d in directions:
            nr, nc = row + d[0], col + d[1]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == "1": #Here, grid is in char remember, int will be false
                self.dfs(nr, nc, visited, grid, vec, row0, col0)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        unique_islands = []  # If need Unique No of Island, use a set to keep only distinct
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    curr_island = []
                    self.dfs(i, j, visited, grid, curr_island, i, j)
                    unique_islands.append(tuple(curr_island))

        return len(unique_islands) #If want to return the indexes, don't return the length
