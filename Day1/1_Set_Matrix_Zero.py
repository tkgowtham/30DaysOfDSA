class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        rows = [1] * r
        cols = [1] * c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        
        
        for i in range(r):
            if rows[i] == 0:
                matrix[i] = [0] * c

        for j in range(c):
            if cols[j] == 0:
                for i in range(r):
                    matrix[i][j] = 0

        return matrix
