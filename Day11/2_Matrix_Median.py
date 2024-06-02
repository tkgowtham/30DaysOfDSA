class Solution:
    def median(self, matrix, R, C):
        def upperBound(arr, x, n):
            low = 0
            high = n - 1
            ans = n
        
            while low <= high:
                mid = (low + high) // 2
                # maybe an answer
                if arr[mid] > x:
                    ans = mid
                    # look for a smaller index on the left
                    high = mid - 1
                else:
                    low = mid + 1  # look on the right
        
            return ans
            
            
        def countSmallerThanEqualToMid(matrix, m, n, mid):
            cnt = 0
            for i in range(m):
                cnt += upperBound(matrix[i], mid, n)
            return cnt

        def findMedian(matrix, m, n):
            low = float('inf')
            high = float('-inf')
            
            for i in range(m):
                low = min(low, matrix[i][0])
                high = max(high, matrix[i][n-1])
                
            req = (n * m) // 2
            while low <= high:
                mid = (low + high) // 2
                smallEqual = countSmallerThanEqualToMid(matrix, m, n, mid)
                if smallEqual <= req:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return low
                
        return findMedian(matrix, R, C)
