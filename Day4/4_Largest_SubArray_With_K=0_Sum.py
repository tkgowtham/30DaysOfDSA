class Solution:
    def maxLen(self, n, arr):
        #Code here
        sums = 0
        longest = 0
        dict1 = {}
        for i in range(n):
            sums += arr[i]
            if sums == 0:
                longest = max(longest, i + 1)
            elif sums not in dict1:
                dict1[sums] = i
            else:
                longest = max(longest, i - dict1[sums]) # Basically, since we found one with same sum, it will cancel out, so a new subarray is formed.
        
        return longest
