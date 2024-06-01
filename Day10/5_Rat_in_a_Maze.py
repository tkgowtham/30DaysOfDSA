#TC = O(4^(m*n)) SC = O(m*n)
class Solution:
    def findPath(self, m, n):
        # code here
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
            
        result = []
        def solve(m, n, row, col, s, visited):
            if row == n - 1 and col == n - 1:
                temp = ''
                for i in s:
                    temp += i
                result.append(temp)
                return
            
            if 0 <= row + 1 < n and m[row + 1][col] == 1 and not visited[row + 1][col]:
                s.append('D')
                visited[row + 1][col] = True
                solve(m, n, row + 1, col, s, visited)
                visited[row + 1][col] = False
                s.pop()
            if 0 <= col + 1 < n and m[row][col + 1] == 1 and not visited[row][col + 1]:
                s.append('R')
                visited[row][col + 1] = True
                solve(m, n, row, col + 1, s, visited)
                visited[row][col + 1] = False
                s.pop()
            if 0 <= row - 1 < n and m[row - 1][col] == 1 and not visited[row - 1][col]:
                s.append('U')
                visited[row - 1][col] = True
                solve(m, n, row - 1, col, s, visited)
                visited[row - 1][col] = False
                s.pop()
            if 0 <= col - 1 < n and m[row][col - 1] == 1 and not visited[row][col - 1]:
                s .append('L')
                visited[row][col - 1] = True
                solve(m, n, row, col - 1, s, visited)
                visited[row][col - 1] = False
                s.pop()
        
        s = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True
        solve(m, n, 0, 0, s, visited)
        return result
