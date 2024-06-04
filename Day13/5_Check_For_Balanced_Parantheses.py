class stack:
    def __init__(self):
        self.arr = []

    def push(self,x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()

class Solution:
    def isValid(self, s: str) -> bool:
        Stack = stack()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                Stack.push(i)
            else:
                v = Stack.pop()
                if v == '(' and i == ')':
                    continue
                elif v == '[' and i == ']':
                    continue
                elif v == '{' and i == '}':
                    continue
                else:
                    return False

        if Stack.pop() == -1:
            return True
        else:
            return False
