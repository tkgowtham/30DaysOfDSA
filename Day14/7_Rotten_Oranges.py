from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh_orange = 0
        count = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_orange += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        while q and fresh_orange > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    q.append([i-1,j])
                    fresh_orange -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    q.append([i+1,j])
                    fresh_orange -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    q.append([i,j-1])
                    fresh_orange -= 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    q.append([i,j+1])
                    fresh_orange -= 1
            minutes += 1

        if fresh_orange == 0:
            return minutes
        else:
            return -1
