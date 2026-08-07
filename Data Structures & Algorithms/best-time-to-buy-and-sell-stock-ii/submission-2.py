class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) not in memo:
                nothing = dp(i + 1, holding)
                something = 0
                if holding:
                    #sell
                    something = prices[i] + dp(i + 1, 0)
                else:
                    something = -prices[i] + dp(i + 1, 1)

                memo[(i, holding)] = max(nothing, something)
            return memo[(i, holding)]
        
        return dp(0, 0)