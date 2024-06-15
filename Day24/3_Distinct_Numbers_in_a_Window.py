#Brute Force
from collections import Counter
class Solution:
	
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		ans = []
		for i in range(len(A)-B+1):
			ans.append( len(Counter(A[i:i+B])) )
		
		return ans

#Optimal Method

class Solution:
	
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		if len(A) < B:
			return []
			
		freq_map = {}
		result = []
		
		for i in range(0, B, 1):
			if A[i] in freq_map:
				freq_map[A[i]] += 1
			else:
				freq_map[A[i]] = 1
				
		result.append(len(freq_map))
		
		for i in range(B, len(A), 1):
			start_element = A[i - B]
			if freq_map[start_element] == 1:
				del freq_map[start_element]
			else:
				freq_map[start_element] -= 1
				
			next_element = A[i]
			if next_element in freq_map:
				freq_map[next_element] += 1
			else:
				freq_map[next_element] = 1
				
			result.append(len(freq_map))
			
		return result	
