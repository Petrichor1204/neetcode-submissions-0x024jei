class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # goal: to find the perimeter of an island where there is only one island in the grid and is formed by cells connecting vertically or horizontally
        # {(0,0), (0,1), (1,0), (2,0), (2,1),(2,2), (3,2), (3,3)} p = 18
        perimeter = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)] #ewns
        visited = set()

        def dfs(r, c):
            nonlocal perimeter
            # base case - isisland if at least one side is water or edge
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                perimeter += 1
                return

            # subproblems
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    dfs(nr, nc)
           

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    dfs(r, c)
                    return perimeter