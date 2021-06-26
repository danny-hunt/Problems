
"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
from random import randint
from typing import List


stock_prices = [randint(4, 20) for _ in range(10)]

def best_return(prices: List[int]) -> int:
    current_lowest = stock_prices[0]
    current_max_return = 0
    for cost in prices:
        if cost < current_lowest:
            current_lowest = cost
        elif cost - current_lowest > current_max_return:
            current_max_return = cost - current_lowest
    return current_max_return

print(stock_prices)
print(best_return(stock_prices))
