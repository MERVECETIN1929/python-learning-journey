class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_number = prices[0]
        max_avr = 0
        for number in prices:
            min_number = min(min_number, number)
            if number-min_number > max_avr:
                max_avr = number-min_number
        return max_avr


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([3, 2, 6, 5, 0, 3]))
print(solution.maxProfit([1, 5, 3, 8, 4, 9]))
