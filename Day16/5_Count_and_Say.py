class Solution:
    def countAndSay(self, n: int) -> str:
        def run(i, n, s):
            if i == n:
                return s
            
            ans = ""
            value = s[0]
            times = 1
                
                
            for index in range(1, len(s)):
                if value == s[index]:
                    times += 1
                else:
                    ans += str(times) + str(value)
                    value = s[index]
                    times = 1

            ans += str(times) + str(value)
                
            return run(i + 1, n, ans)
    
        return run(1, n, "1")
