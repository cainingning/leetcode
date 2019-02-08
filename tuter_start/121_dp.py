class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_num = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - min_num > max_profit:
                max_profit = prices[i] - min(prices[:i])
            if prices[i] < min_num:
                min_num = prices[i]

        return max_profit