class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        output = 0
        for price in prices:
            minprice = min(minprice,price)
            output = max(output, price - minprice)
        return output