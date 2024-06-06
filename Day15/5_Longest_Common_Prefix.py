class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        length = [len(i) for i in strs]
        l = min(length)
        i = 0
        while i < l:
            prev = None
            flag = False
            for s in strs:
                if prev == None:
                    prev = s[i]
                elif prev == s[i]:
                    continue
                else:
                    flag = True
                    break
            if flag == False:
                ans += prev
            else:
                break
            i += 1
        
        return ans
