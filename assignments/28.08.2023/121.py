class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        least = 10000
        lar = 0
        for i in range(0,n):

            if prices[i] < least:
                least = prices[i]
            if prices[i] - least > lar:
                lar = prices[i] - least 
                
        return lar