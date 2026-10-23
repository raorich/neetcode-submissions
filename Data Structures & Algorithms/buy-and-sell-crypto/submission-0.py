class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=prices
        profit=0
        for daybuy in range(len(prices)):
            for ds in range(daybuy,len(prices),1):
                if prices[ds]-prices[daybuy]>profit:
                    profit = prices[ds]-prices[daybuy]
        return profit
        