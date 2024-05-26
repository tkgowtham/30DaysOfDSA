#O(2N) Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
            
        HashSet = set(s[0])
        l = 0
        r = 1
        count = 0
        while l < len(s) and r < len(s):
            if s[r] not in HashSet:
                count = max(count, r - l + 1)
                HashSet.add(s[r])
                r += 1
            else:
                HashSet.remove(s[l])
                l += 1
        return count

  
