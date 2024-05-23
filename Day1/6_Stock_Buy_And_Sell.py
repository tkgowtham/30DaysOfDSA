from sys import maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = 0
        minPrice = maxsize
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfits = max(maxProfits, prices[i] - minPrice)

        return maxProfits
