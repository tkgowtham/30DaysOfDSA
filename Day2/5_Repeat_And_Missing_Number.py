#Approach 1 : Linear Time and Linear Space
#Completely Working
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        freq = [0] * (len(A) + 1)
        for i in range(len(A)):
            freq[A[i]] += 1
        freq.pop(0) # since we are taking from 1 to n
        return [freq.index(max(freq)) + 1, freq.index(min(freq)) + 1]

#Approach 2 : Linear Time and Constant Space
#Few cases not working
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        Sn = (n * (n + 1)) / 2
        S2n = Sn * ((2*n + 1) / 3)  # n * (n + 1) * (2n + 1) / 6
        S = 0
        S2 = 0
        for i in range(n):
            S += A[i]
            S2 += (A[i] * A[i])
        val1 = Sn - S     # x - y = Sn - S
        val2 = S2n - S2   # X2 - Y2 = S2n - S2 = (x - y) * (x + y)
        val2 = val2 / val1  # x + y = (S2n - S2) / (x - y)
        x = (val1 + val2) / 2 # solving x + y and x - y 
        y = x - val1
        return [int(y), int(x)]
