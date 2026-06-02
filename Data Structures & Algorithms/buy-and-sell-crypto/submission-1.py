class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        difference = 0
        for i in range(len(prices)-1, 0, -1):
            if prices[i] >= temp:
                temp = prices[i]
            if (temp - prices[i-1]) > difference:
                difference = temp - prices[i-1]
        return difference

        