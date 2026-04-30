class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        #                l 
        #                r
        # max left = 3
        # max right = 2
        # total = 9
        # left heights = [0,0,2,2,3,3,3,3,3,3]
        # right heights = [3,3,3,3,3,3,3,2,1,0]
        # min height = [0,0,2,2,3,3,3,2,1,0]
        # each bar   = [0,0,2,0,2,3,2,0,0,0] 
        # area = height of min bar * width
        # how much water sits on each individual bar?
        # min of (total height of bar from left and height of bar from right)
        # each bar = max(0, (min(maxleft, maxright) - height[i]))
        # moving = if left smaller, l += 1 else r -= 1
        # if we didn't move from a position, don't calculate its water
        
        total_amount = 0
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while l < r:
            if height[l] <= height[r]:
                max_left = max(max_left, height[l])
                total_amount += max(0, (max_left - height[l]))
                l += 1
            else:
                max_right = max(max_right, height[r])
                total_amount += max(0, (max_right - height[r]))
                r -= 1
        return total_amount
        



