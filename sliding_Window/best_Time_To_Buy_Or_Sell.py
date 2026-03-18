from typing import List

def maxProfit(prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        return max_profit


print(maxProfit([10,1,5,6,7,1]))