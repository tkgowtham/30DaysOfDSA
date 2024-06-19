class Solution:
    def mcm(self, arr, i, j, dp):
        if i == j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        mini = float('inf')
        
        for k in range(i , j):
            ans = self.mcm(arr, i, k, dp) + self.mcm(arr, k + 1, j, dp) + (arr[i - 1] * arr[k] * arr[j])

            mini = min(mini, ans)
          
        dp[i][j] = mini  
        return dp[i][j]
        
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1 for i in range(N)] for j in range(N)]
        i = 1
        j = N - 1
        return self.mcm(arr, i , j, dp)
