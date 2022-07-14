class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])

            if prices[left] > prices[right]:
                left += 1
            else:
                right += 1
        return profit
