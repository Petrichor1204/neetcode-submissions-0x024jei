class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # goal: return the max amount of water two bars can contain
        # area = width * height => min(height a, height b)
        # width = r - l
        # [1,7,2,5,4,7,3,6] 6 * 6 = 36
        #    l
        #              r
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            max_area = max(max_area, width * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area