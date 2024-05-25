class Solution: # O(N*M)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                for j in range(-1,-len(matrix[i])-1,-1):
                    if target == matrix[i][j]:
                        return True
                return False

