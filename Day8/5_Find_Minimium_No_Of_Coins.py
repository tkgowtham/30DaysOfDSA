amount = int(input())
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
no_of_coins = 0
for i in range(len(coins)-1, -1, -1):
  while amount >= coins[i]:
    no_of_coins += 1
    amount -= coins[i]

print(no_of_coins)
