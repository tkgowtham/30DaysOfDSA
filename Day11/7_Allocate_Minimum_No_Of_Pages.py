class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def countStudent(self, arr, pages):
		students = 1
		pagesStudent = 0
		for i in range(len(arr)):
			if pagesStudent + arr[i] <= pages:
				pagesStudent += arr[i]
			else:
				students += 1
				pagesStudent = arr[i]
				
		return students
	
	def books(self, A, B):
		high = sum(A)
		if B == 1:
			return high
		
		low = max(A)
		
		n = len(A)
		m = B 
		
		if m > n:
			return -1
			
		while low <= high:
			mid = (low + high) // 2
			students = self.countStudent(A, mid)
			if students > m:
				low = mid + 1
			else:
				high = mid - 1
				
		return low
