class Solution:
    def isSubsetSum (self, n, arr, k):
        # code here 
        prev = [False] * (k + 1)
        prev[0] = True
        if arr[0] <= k:
            prev[arr[0]] = True
            
        for i in range(1, n):
            cur = [False] * (k + 1)
            cur[0] = True
            for target in range(1, k + 1):
                not_taken = prev[target]
                taken = False
                
                if arr[i] <= target:
                    taken = prev[target - arr[i]]
                    
                cur[target] = not_taken or taken
                
                
            prev = cur
            
        return prev[k]
