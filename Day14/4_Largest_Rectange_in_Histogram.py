from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        maxA = 0
        n = len(heights)
        for i in range(n+1):
            while stack and ( i == n or heights[stack[-1]] >= heights[i]):
                h = heights[stack[-1]]
                stack.pop()
                width = None
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxA = max(maxA, width * h)
            stack.append(i)
        return maxA
