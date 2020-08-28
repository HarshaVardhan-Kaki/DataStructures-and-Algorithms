# leetcode

# O(n) time and O(1) space
# n is length of array
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit