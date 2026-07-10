class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                res = max(res, prices[i] - curr)
        
        return res