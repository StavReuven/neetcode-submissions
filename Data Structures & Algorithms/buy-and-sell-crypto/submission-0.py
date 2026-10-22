class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        curMax = 0
        cur = 0

        while cur < len(prices):
            if prices[cur] < prices[buy]:
                buy = cur
                continue
            curMax = max(curMax, prices[cur] - prices[buy])
            cur += 1


        return curMax