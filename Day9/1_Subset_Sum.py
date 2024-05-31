#TC = O(2^N) power set is computer SC = O(2^N)

class Solution:
    
	def subsetSums(self, arr, n):
	    result = []
	    
	    def findS(arr, ind, n, sums):
            if n == ind:
                result.append(sums)
                return
                
            findS(arr, ind + 1, n, sums + arr[ind])
            findS(arr, ind + 1, n, sums)
            
		# code here
		findS(arr, 0, n, 0)
		return result
