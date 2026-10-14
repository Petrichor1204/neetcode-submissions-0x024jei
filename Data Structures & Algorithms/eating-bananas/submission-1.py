class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # goal: find the minimum num of bananas per hour to eat all bananas within h hours 
        # mid = 1
        # [1,4,3,2] time = 6

                
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            
            time = 0
            for pile in piles:
                if time > h:
                    break
                while pile > 0:
                    if pile <= mid:
                        time += 1
                        pile = 0
                    else:
                        time += pile // mid
                        pile = pile % mid
            if time <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
                
            
            