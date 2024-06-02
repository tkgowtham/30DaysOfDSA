class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1
            
            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n else float('inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = arr2[mid2] if mid2 < m else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return -1
