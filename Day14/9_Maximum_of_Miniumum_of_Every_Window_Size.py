#My Brute Force Approach
from collections import deque
def maxMinWindow(arr, n):
    def minWindow(arr, k):
        deque_window = deque()
        res = []
        
        for index, num in enumerate(arr):
            if deque_window and deque_window[0] == index - k:
                deque_window.popleft()
            
            while deque_window and arr[deque_window[-1]] > num:
                deque_window.pop()
            
            deque_window.append(index)
            
            if index >= k - 1:
                res.append(arr[deque_window[0]])
        
        return res

    res = []
    for i in range(1, n+1):
        res.append(max(minWindow(arr, i)))
    
    return res


#Optimised Approach
def maxMinWindow(arr, n):

    left = [-1] * n
    right = [n] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
      
    stack.clear()
  
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    ans = [-float('inf')] * (n + 1)
  
    for i in range(n):
        length = right[i] - left[i] - 1
        ans[length] = max(ans[length], arr[i])

    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

    return ans[1:]
