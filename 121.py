class Solution:

    def maxProfit(self,prices: list[int]) -> int:

        # buy the stock on a day and sell it later date to maximise pofit
        # [7,1,5,3,6,4]
        # buy on 1 sell on 6 max profit =5
        # [7,6,4,3,2,1]
        # buy no day all is loss
        cheapest_price:int = prices[0]
        max_profit:int     = 0

        for price in prices:
            if price < cheapest_price:
                cheapest_price = price
            elif (price-cheapest_price)>max_profit:
                max_profit = price - cheapest_price
        
        return max_profit
s = Solution()
print('[7,1,5,3,6,4] -> ',s.maxProfit(prices = [7,1,5,3,6,4]))
print('[7,6,4,3,1] -> ',s.maxProfit(prices = [7,6,4,3,1]))