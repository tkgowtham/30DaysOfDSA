#TC = O(N! * N) SC = O(N)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = []
        for i in range(n):
            board.append(['.']*n)
        
        leftRow = [0] * n
        upperLeftDiagonal = [0] * (2 * n - 1)
        lowerLeftDiagonal = [0] * (2 * n - 1)

        col = 0

        def solve(col, board, ans, leftRow, upperLeftDiagonal, lowerLeftDiagonal, n):
            if col == n:
                temp = []
                for i in board:
                    s = ''
                    for j in i:
                        s += j
                    temp.append(s)
                ans.append(temp.copy())
                return

            for row in range(n):
                if leftRow[row] == 0 and lowerLeftDiagonal[col + row] == 0 and upperLeftDiagonal[n - 1 + col - row] == 0:
                    
                    board[row][col] = 'Q'
                    leftRow[row] = 1
                    lowerLeftDiagonal[col + row] = 1
                    upperLeftDiagonal[n - 1 + col - row] = 1

                    solve(col + 1, board, ans, leftRow, upperLeftDiagonal, lowerLeftDiagonal, n)

                    board[row][col] = '.'
                    leftRow[row] = 0
                    lowerLeftDiagonal[col + row] = 0
                    upperLeftDiagonal[n - 1 + col - row] = 0


        solve(col, board, ans, leftRow, upperLeftDiagonal, lowerLeftDiagonal, n)
        return ans


#TC = O(N! * N) SC = O(N^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = []
        for i in range(n):
            board.append(['.']*n)

        col = 0

        def isSafe(col, row, board, n):
            for i in range(col):
                if board[row][i] == 'Q':
                    return False

            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True 

        def solve(col, board, ans, n):
            if col == n:
                temp = []
                for i in board:
                    s = ''
                    for j in i:
                        s += j
                    temp.append(s)
                ans.append(temp.copy())
                return

            for row in range(n):
                if isSafe(col, row, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, ans, n)
                    board[row][col] = '.'


        solve(col, board, ans, n)
        return ans
