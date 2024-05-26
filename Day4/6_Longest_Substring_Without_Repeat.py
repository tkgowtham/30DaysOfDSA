#O(2N) Approach --> This is more efficent method in terms of time and space.
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

  
#O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        dict1 = {}
        l = r = 0
        n = len(s)
        length = 0
        while r < n:
            if s[r] in dict1:
                l = max(l, dict1[s[r]] + 1)
            
            dict1[s[r]] = r
            length = max(length, r - l + 1)
            r += 1

        return length
