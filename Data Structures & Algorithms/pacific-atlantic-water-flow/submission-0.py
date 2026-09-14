class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # goal: return a list of cells whose water can flow into both oceans
  
        rows = len(heights)
        cols = len(heights[0])
        result = []
        # for each cell, dfs to check if can flow into both
        # {(0,0), (0,1)} (-1, 0) isP= t
        
        def canFlow(r, c, seen):
            nonlocal is_pacific
            nonlocal is_atlantic

            seen.add((r,c))
            adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            
            for rr, cc in adj:
                # if out of bounds
                if rr < 0 or cc < 0:
                    is_pacific = True
                    continue

                if rr == rows or cc == cols:
                    is_atlantic = True
                    continue
   
                if heights[rr][cc] > heights[r][c] or (rr, cc) in seen:
                    continue
                canFlow(rr, cc, seen)

            return is_pacific and is_atlantic

        for r in range(rows):
            for c in range(cols):
                is_pacific = False
                is_atlantic = False
                if canFlow(r, c, set()) == True:
                    result.append([r, c])

        return result
# (0,0)