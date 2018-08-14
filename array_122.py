class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        允许多次交易一只股票。贪心算法，只要后一天比前一天价格高就可以产生一次买卖
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([5, 4, 3]))

