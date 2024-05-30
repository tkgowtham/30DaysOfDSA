amount = int(input())
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
no_of_coins = 0
for i in range(len(coins)-1, -1, -1):
  while amount >= coins[i]:
    no_of_coins += 1
    amount -= coins[i]

print(no_of_coins)

#Greedy Approach Not Always for works for all conditions
def coinChange(coins, amount):
    if amount == 0:
        return 0
        
    coins.sort()
    no_of_coins = 0
    for i in range(len(coins)-1, -1, -1):
        while amount >= coins[i]:
            print(coins[i]," ",amount)
            amount -= coins[i]
            no_of_coins += 1

    return no_of_coins if no_of_coins > 0 and amount == 0 else -1

#DP Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
