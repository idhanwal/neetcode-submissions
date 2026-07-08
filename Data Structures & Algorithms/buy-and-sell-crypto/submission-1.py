class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i, n in enumerate(prices):
            buy = n
            sell_pos = i + 1
            while sell_pos < len(prices) and prices[sell_pos] > buy:
                max_diff = max(max_diff, prices[sell_pos] - buy)
                sell_pos += 1
        return max_diff