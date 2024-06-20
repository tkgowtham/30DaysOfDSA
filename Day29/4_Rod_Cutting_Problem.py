def cutRod(price, n):

    # Initialize the dp array
    dp = [0] * (n + 1)

    # Process for all lengths from 1 to n
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i - j - 1])
        dp[i] = max_val

    return dp[n]
