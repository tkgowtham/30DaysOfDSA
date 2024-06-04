def insert(s, x):
    if not s or x > s[-1]:
        s.append(x)
        return

    temp = s.pop()
    insert(s, x)
    s.append(temp)

def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    if stack:
        x = stack.pop()
        sortStack(stack)
        insert(stack, x)
