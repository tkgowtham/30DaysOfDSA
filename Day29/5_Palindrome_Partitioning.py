class Solution:
    def isPalindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def f(self, i, n, string, dp):
        if i == n:
            return 0
            
        if dp[i] != -1:
            return dp[i]
            
        minCost = float('inf')
        for j in range(i, n):
            if self.isPalindrome(i, j, string):
                cost = 1 + self.f(j + 1, n, string, dp)
                minCost = min(minCost, cost)
                
        dp[i] = minCost
        return dp[i]
                
    def palindromicPartition(self, string):
        n = len(string)
        dp = [-1] * n
        return self.f(0, n, string, dp) - 1
