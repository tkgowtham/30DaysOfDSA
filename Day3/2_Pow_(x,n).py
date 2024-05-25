class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        temp = n
        if temp < 0: #convert to positive power
            temp *= -1

        while temp > 0:
            if temp % 2 != 0: #if odd
                ans *= x
                temp -= 1
            else: #if even
                x *= x
                temp //= 2

        if n < 0:
            ans = 1.0 / ans #if neg power caculating inverse
        
        return ans
#Using Binary Exponential Method
# O(logn)
