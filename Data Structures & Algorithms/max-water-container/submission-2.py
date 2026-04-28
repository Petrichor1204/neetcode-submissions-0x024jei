class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6] n = 8
        #    l 
        #    r
        # areas = 7, 36, 15, 28, 12, 10, 2
       
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(area, max_area) 
            # then determine which pointer to move based on smaller 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        
      
