#Linear Search TC = O(m)
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    for i in range(1,m+1):
        v = pow(i,n)
        if v == m:
            return i
        elif v > m:
            break
    
    return -1
    pass

#Binary Search TC = O(logN)
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    def power(mid, n):
        ans = 1
        for i in range(1, n + 1):
            ans = ans * mid
            if ans > m:
                return 1

        if ans == m:
            return 0

        return -1

    def solve(n,low, high):
        if low > high:
            return -1
            
        mid = int((low + high) // 2)
        #print(mid)
        val = power(mid, n)
        if val == 0:
            return mid
        elif val == 1:
            return solve(n, low, mid - 1)
        elif val == -1:
            return solve(n, mid + 1, high)

    return solve(n, 0, m)
