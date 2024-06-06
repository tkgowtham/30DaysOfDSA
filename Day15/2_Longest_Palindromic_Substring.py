class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            max_len = len1 if len(len1) > len(len2) else len2
            
            if len(max_len) > end - start:
                start = i - ((len(max_len) - 1) // 2)
                end = i + (len(max_len) // 2)
        
        return s[start:end + 1]

        #Code to find SUBSEQUENCE and Length
        '''if len(s) == 0:
            return ""
        
        if len(s) == 1:
            return s
        def findLongestPalindrome(s, i, j, lookup):
            if i > j:
                return 0
            
            if i == j:
                return 1

            key = str(i) + "|" + str(j)

            if key not in lookup:
                if s[i] == s[j]:
                    lookup[key] = findLongestPalindrome(s, i + 1, j - 1, lookup) + 2
                else:
                    lookup[key] = max(findLongestPalindrome(s, i, j - 1, lookup),
                                      findLongestPalindrome(s, i + 1, j, lookup))
            
            return lookup[key]

        def LCSlength(x, y, n, lookup):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if x[i - 1] == y[j - 1]:
                        lookup[i][j] = lookup[i - 1][j - 1] + 1
                    else:
                        lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

        def findLongestPalindrome(x, y, m, n, lookup):
            if m == 0 or n == 0:
                return ""
            
            if x[m - 1] == y[n - 1]:
                return findLongestPalindrome(x, y, m - 1, n - 1, lookup) + x[m - 1]
            if lookup[m - 1][n] > lookup[m][n - 1]:
                return findLongestPalindrome(x, y, m - 1, n, lookup)
            return findLongestPalindrome(x, y, m, n - 1, lookup)

        r = s[::-1]
        n = len(s)
        lookup = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        LCSlength(s, r, n, lookup)

        res = findLongestPalindrome(s, r, n, n, lookup)
        return res if res else s[0]'''
