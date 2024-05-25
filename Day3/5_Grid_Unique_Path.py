#Using DP and Recursion O(n*m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPath(i, j, m, n, dp):
            if i >= m or j >= n:
                return 0
            if i == (m - 1) and j == (n - 1):
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = countPath(i + 1, j, m, n, dp) + countPath(i, j + 1, m, n, dp)
                return dp[i][j]

        dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]
        num = countPath(0, 0, m, n, dp)
        if m == 1 or n == 1:
            return num
        return dp[0][0]

#Using combinations formula O(m-1) or O(n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        r = min(m - 1, n - 1)
        res = 1
        for i in range(1, r + 1):
            res = res * (N - r + i) / i
        return int(res)
