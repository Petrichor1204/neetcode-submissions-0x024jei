class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s, f = 0, 1
        max_profit = 0
    
        while f < len(prices):
            if prices[s] < prices[f]:
                max_profit = max(max_profit, prices[f] - prices[s])
            else:
                s = f
            f += 1
        return max_profit