class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def LPS(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps[-1]
        
        s = A + "#" + A[::-1]
        
        longest_palindromic_suffix_length = LPS(s)
        
        return len(A) - longest_palindromic_suffix_length  
