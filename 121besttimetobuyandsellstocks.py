def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max (max_profit,current_profit)
            else:
                buy = sell
            sell += 1
        return max_profit