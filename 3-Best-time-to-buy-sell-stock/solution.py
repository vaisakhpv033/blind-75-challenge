# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for val in prices:
            profit = val - buy_price
            if profit > max_profit:
                max_profit = profit
            if val < buy_price:
                buy_price = val
        return max_profit