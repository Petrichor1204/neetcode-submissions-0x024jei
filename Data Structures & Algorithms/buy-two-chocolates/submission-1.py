class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # goal: to buy two chocolates with the minimum amount and still have some amount left over, return the amount left over
        # [2,5,1,2], money = 3
        #      l
        #        r
        min_sum = float('inf')

        l, r = 0, len(prices) - 1
        while l < r:
            curr_sum = prices[l] + prices[r]
            min_sum = min(curr_sum, min_sum)
            if prices[l] < prices[r]:
                r -= 1
            else:
                l += 1
                    
        return money - min_sum if money - min_sum >= 0 else money
