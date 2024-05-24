class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        freq = [0] * (len(A) + 1)
        for i in range(len(A)):
            freq[A[i]] += 1
        freq.pop(0) # since we are taking from 1 to n
        return [freq.index(max(freq)) + 1, freq.index(min(freq)) + 1]
