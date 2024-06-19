class Solution:
    def f(self, ind, prev_ind, arr, n, dp):
        if ind == n:
            return 0
        if dp[ind][prev_ind+1] != -1:
            return dp[ind][prev_ind+1]
        l = 0 + self.f(ind + 1, prev_ind, arr, n, dp)
        if prev_ind == -1 or arr[ind] > arr[prev_ind]:
            l = max(l, 1 + self.f(ind+1, ind, arr, n, dp))
        dp[ind][prev_ind+1] = l
        return dp[ind][prev_ind+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for i in range(n + 1)] for _ in range(n)]
        return self.f(0, -1, nums, n, dp)
