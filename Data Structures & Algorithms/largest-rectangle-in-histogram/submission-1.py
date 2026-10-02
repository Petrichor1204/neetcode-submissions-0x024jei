class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # goal: to return the maximum area of rectangle that can be formed from heights
        # heights = [7,1,7,2,2,4]
        #            i
        #              k
        # [4,3]
        # [1,4,1,2,1,0]
        # [1,1,1,,0,1]
        # max areas = [7,6,7,8,8,4]
        # max area = 1

        # start at each position
        # go left to find how many are bigger or eq
        # if you hit smaller, stop counting
        max_area = 0
        n = len(heights)
        
        count_left = [i + 1 for i in range(n)] 
        count_right = [n - i for i in range(n)] 

        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                count_right[idx] = i - idx
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                count_left[idx] = idx - i
            stack.append(i)

        for i in range(n):
            total_count = count_left[i] + count_right[i]
            curr_area = heights[i] * (total_count - 1) 
            max_area = max(max_area, curr_area)

            
        return max_area

