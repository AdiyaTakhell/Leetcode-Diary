def maxProfit(prices: list[int]) -> int:
    i, j = 0, 1
    max_profit = 0
    while j < len(prices):
        if prices[i] < prices[j]:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
        else:
            i = j
        j += 1
    return max_profit
