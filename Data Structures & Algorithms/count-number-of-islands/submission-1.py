class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        count = 0
        visited = set()
        cols = len(grid[0])
        rows = len(grid)

        def dfs(r, c):      
            if not (0 <= r < rows and 0 <= c < cols):
                return 
            if (r, c) in visited or grid[r][c] == "0":
                return 
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
                    
            return 

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
