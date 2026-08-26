class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(prices[j] - prices[i], max_profit)

        # min_price = prices[0]
        # for i in range(1, len(prices)):
        #     if prices[i] > min_price:
        #         profit = prices[i] - min_price
        #     else:
        #         profit = 0
        #         min_price = prices[i]
        #     max_profit = max(profit, max_profit)

        max_profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)

        return max_profit