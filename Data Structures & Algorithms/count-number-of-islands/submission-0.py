class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        count = 0
        visited = set()
        cols = len(grid[0])
        rows = len(grid)

        def dfs(r, c):      
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) in visited or grid[nr][nc] == "0":
                        continue
                    visited.add((nr, nc))
                    dfs(nr, nc)
            return 

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        

        

        return count
