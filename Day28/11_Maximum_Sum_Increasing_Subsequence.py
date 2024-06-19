class Solution:
	def maxSumIS(self, arr, n):
		# code here
        dp = [0] * n
        
        for i in range(n):
            dp[i] = arr[i]
        
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                    dp[i] = dp[j] + arr[i]
        
        return max(dp)
