class Solution: # O(N*M)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                for j in range(-1,-len(matrix[i])-1,-1):
                    if target == matrix[i][j]:
                        return True
                return False

# Using Binary Search -- doesn't work for all cases -- O(log(M*N))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n*m - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // 2
            col = mid % 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
