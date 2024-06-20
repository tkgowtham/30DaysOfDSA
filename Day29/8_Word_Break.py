class Solution:
    def func(self, word, dp, ind, s):
        n = len(s)
        if ind == n:
            return True
        if dp[ind] != -1:
            return dp[ind]
        if s[ind:] in word:
            return True
        
        for j in range(ind, n):
            temp = s[ind:j + 1]
            if temp in word and self.func(word, dp, j + 1, s):
                dp[ind] = 1
                return dp[ind]

        dp[ind] = 0
        return dp[ind]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word = set(wordDict)
        n = len(s)
        dp = [-1] * n
        return self.func(word, dp, 0, s)
