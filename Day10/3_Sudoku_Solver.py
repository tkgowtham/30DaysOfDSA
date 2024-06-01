#TC = O(9^(n ^ 2)) SC = O(1)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isSafe(board, row, col, num):
            #Check Col and Row
            for temp in range(9):
                if board[temp][col] == num or board[row][temp] == num:
                    return False

            #Check Box
            startRow = 3 * (row // 3)
            startCol = 3 * (col // 3)
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False
            return True


        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in range(1,10):
                            if isSafe(board, row, col, str(num)):
                                board[row][col] = str(num)
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False

            return True
        
        return solve(board)
