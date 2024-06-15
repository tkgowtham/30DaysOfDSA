#Use this BFS Approach, memory efficient and time efficent.
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        startColor = image[sr][sc]
        n = len(image)
        m = len(image[0])
        queue = deque([(sr, sc)])

        while queue:
            row, col = queue.popleft()
            if image[row][col] == startColor:
                direction = ((1,0),(0,1),(-1,0),(0,-1))
                image[row][col] = color
                for i in direction:
                    nr = row + i[0]
                    nc = col + i[1]
                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == startColor:
                        queue.append((nr, nc))

        return image
