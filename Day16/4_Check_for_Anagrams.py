#My Code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def updateDict(string):
            d = {}
            for i in string:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            return d

        dict_s = updateDict(s)
        dict_t = updateDict(t)

        if len(dict_s) != len(dict_t):
            return False
        
        for i in dict_s:
            if i not in dict_t or dict_s[i] != dict_t[i]:
                return False

        return True

#Simpler Easier Code
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
