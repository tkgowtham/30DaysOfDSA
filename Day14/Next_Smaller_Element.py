class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        if len(A) == 1:
            return [-1]
        if len(A) == 0:
            return []
        res = []
        stack = []
        for num in A:
            while stack and stack[-1] >= num:
                stack.pop()
                
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            
            stack.append(num)
        return res
