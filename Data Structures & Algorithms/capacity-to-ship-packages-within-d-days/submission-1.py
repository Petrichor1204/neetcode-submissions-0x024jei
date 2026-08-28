class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # goal: find the smallest weight the ship can have in order to carry all the weights within the given num of days

        # finding the minimum weight - return a weight
        #weights=[3,2,2,4,1,4] days=3  d = 0 mw = 0
        #         i
        # l = 4   r = 9  w = 10  cw = 0

        min_weight = sum(weights)
    
        # trying each min weight to carry weights withing d days
        # use weight to test on the data
        
        left = max(weights)
        right = sum(weights)

        while left <= right:
            weight = (left + right) // 2

            curr_weights = 0
            i = 0
            d = 0
            while i < len(weights):
                if d > days:
                    left = weight + 1
                    break

                elif weights[i] > weight:
                    left = weight + 1, right
                    break

                elif curr_weights + weights[i] > weight:
                    d += 1
                    curr_weights = 0

                else:
                    curr_weights += weights[i]
                    i += 1

            d += 1
            if d <= days:
                min_weight = min(min_weight, weight)
                right = weight - 1
            else:
                left = weight + 1

        return min_weight
    

