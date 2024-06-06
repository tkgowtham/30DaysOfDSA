from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = deque()
        res = ''
        for i in range(len(s)):
            if s[i] == ' ':
                stack.append(res)
                res = ''
            else:
                res +=  s[i]
        stack.append(res)
        res = ''
        while len(stack) > 1:
            v = stack.pop()
            if v != "":
                res += v + " "
        v = stack.pop()
        if v != "":
            res += v
        res = res.strip()
        return res
