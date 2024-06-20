class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        n = len(grid)
        m = len(grid[0])
        prev = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[j] = grid[i][j]
                else:
                    up = left = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up = float('inf')

                    if j > 0:
                        left += prev[i]
                    else:
                        left = float('inf')

                    temp[j] = min(up, left)

            prev = temp

        return prev[m - 1]
