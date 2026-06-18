class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxDif = 0
        while(right < len(prices)):
            difference = prices[right] - prices[left]
            if(difference < 0):
                left = right
            elif(maxDif < difference):
                maxDif = difference
            right += 1
        return maxDif


        


        