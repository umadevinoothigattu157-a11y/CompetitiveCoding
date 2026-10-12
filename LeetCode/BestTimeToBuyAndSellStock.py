class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-mini)
            mini = min(mini,prices[i])
        return profit
