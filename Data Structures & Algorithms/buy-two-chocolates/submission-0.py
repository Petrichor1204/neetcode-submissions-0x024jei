class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # goal: to buy two chocolates with the minimum amount and still have some amount left over, return the amount left over
        min_sum = float('inf')

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                curr_sum = prices[i] + prices[j]
                min_sum = min(min_sum, curr_sum)
                    
        return money - min_sum if money - min_sum >= 0 else money
