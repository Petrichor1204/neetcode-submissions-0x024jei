class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return the biggest area of island in grid
        max_area = 0
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)] #ewns
        # a = 6, m = 6
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
         
      

            # continuation
            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area
