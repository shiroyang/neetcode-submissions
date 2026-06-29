class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = []
        for price in prices:
            if not cur_min: cur_min.append(price)
            else: cur_min.append(min(cur_min[-1], price))
        ans = 0
        for price, min_price in zip(prices, cur_min):
            ans = max(ans, price - min_price)
        return ans