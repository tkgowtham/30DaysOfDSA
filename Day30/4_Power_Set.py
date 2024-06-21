class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		ans = []
		def solve(i, s, f):
		    if i == len(s):
		        if f:
		            ans.append(f)
		        return
		   
		    solve(i + 1, s, f + s[i])
		    solve(i + 1, s, f)
		   
	    f = ""
	    solve(0, s, f)
	    ans.sort()
	    return ans
