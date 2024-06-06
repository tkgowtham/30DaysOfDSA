#Rabin Karp
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b:
            return 1
        
        count = 1
        source = a
        while len(source) < len(b):
            count += 1
            source += a
        
        if source == b:
            return count
        
        if self.rabin_karp(source, b) != -1:
            return count
        
        if self.rabin_karp(source + a, b) != -1:
            return count + 1

        return -1

    def rabin_karp(self, source, target):
        if source == "" or target == "":
            return -1

        m = len(target)
        power = 1
        base = 1000000
        for i in range(m):
            power = (power * 31) % base

        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i])) % base

        hashCode = 0
        for i in range(len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % base
            if i < m - 1:
                continue
            if i >= m:
                hashCode = (hashCode - ord(source[i - m]) * power) % base
            if hashCode < 0:
                hashCode += base
            if hashCode == targetCode:
                if source[i - m + 1: i + 1] == target:
                    return i - m + 1
        
        return -1

  #My method --> Leetcode giving much efficient time complexity
  class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b:
            return 1
        
        count = 1
        source = a
        while len(source) < len(b):
            count += 1
            source += a
        
        if b in source:
            return count
        
        if b in source + a:
            return count + 1

        return -1
