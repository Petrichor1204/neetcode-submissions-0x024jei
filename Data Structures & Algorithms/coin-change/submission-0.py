class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create the array of size amount + 1 (start from 0)
        # coins = [1,5,10], amount = 12
        # coins=[2] amount=3
        #        c
        # [0, 4, 4, 4]
        #                                      a
        array = [amount + 1] * (amount + 1)
        array[0] = 0

        # go through each num from 1 to amount
        for a in range(1, len(array)):
            for coin in coins:
                if a - coin >= 0:
                    array[a] = min(array[a], array[a - coin] + 1)
        return array[amount] if array[amount] != amount + 1 else -1
       