class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(0, len(prices)):
            j = i + 1
            while j < len(prices):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])
                j += 1
        return profit



        