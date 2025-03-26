class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0  # Hata önleme

        total_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > min_price:
                total_profit += prices[i] - min_price
            min_price = prices[i]

        return total_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max_avr = 0
#         total = 0
#         min_value = prices[0]
#         last_sell_price = 0
#         for price in prices:
#             if price < min_value:
#                 min_value = price
#             if price - min_value > max_avr:
#                 max_avr = price - min_value
#                 last_sell_price = price
#             if max != 0 and price < last_sell_price:
#                 total += max_avr
#                 max_avr = 0
#                 min_value = price
#         if max_avr:
#             total += max_avr
#         return total
