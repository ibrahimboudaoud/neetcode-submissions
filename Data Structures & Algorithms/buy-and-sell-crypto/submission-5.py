class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDate = 0
        sellDate = 1

        while(sellDate < len(prices)):
            profit = prices[sellDate] - prices[buyDate]
            maxProfit = max(profit, maxProfit)
            if(prices[buyDate] > prices[sellDate]):
                buyDate = sellDate
            sellDate += 1

        return maxProfit
            

        