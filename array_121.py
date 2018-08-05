class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        pre_low_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - pre_low_price > max_profit:
                max_profit = prices[i] - pre_low_price
            if prices[i] < pre_low_price:
                pre_low_price = prices[i]

        return max_profit
