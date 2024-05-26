class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):         
        xr = 0
        count = 0
        dict1 = {0 : 1}
        for i in range(len(A)):
            xr = xr ^ A[i]
            x = xr ^ B
            count += dict1.get(x, 0) # get value of x if not there put x with value 0
            dict1[xr] = dict1.get(xr, 0) + 1
        
        return count
