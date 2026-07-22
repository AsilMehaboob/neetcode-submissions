class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        maxprofit=0
        
        for j in range(len(prices)):
            if prices[j]>prices[i]:
                profit=prices[j]-prices[i]
                maxprofit=max(maxprofit,profit)
            else:
                i=j
        return maxprofit