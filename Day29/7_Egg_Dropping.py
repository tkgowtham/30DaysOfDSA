class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        dp = [[0 for x in range(n + 1)] for y in range(k + 1)]
        m = 0
        while dp[m][n] < k:
            m += 1
            for x in range(1, n + 1):
                dp[m][x] = 1 + dp[m - 1][x - 1] + dp[m - 1][x]
        return m
