def maxProfit(values, weights, n, w):

    # Write your code here
    prev = [0] * (w + 1)

    for i in range(weights[0], w + 1):
        prev[i] = values[0]

    for ind in range(1, n):
        for cap in range(w, -1, -1):
            notTaken = 0 + prev[cap]
            taken = float('-inf')
            if weights[ind] <= cap:
                taken = values[ind] + prev[cap - weights[ind]]
            
            prev[cap] = max(notTaken, taken)
    
    return prev[w]
