from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # goal: return the same grid where each land cell is filled with dist to nearest treasure or inf if impossible
        # mulitisource bfs - q 
        q = deque()
        seen = set()
        INF = (2 **31) - 1

        # [(0, 2, 0), (3, 0, 0)] {(0,2)}

        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
    
        # view each treasure and its neighbors while keeping distance
        while q:
            r, c, d = q.popleft()
            adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            for rr, cc in adj:
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == INF:
                    grid[rr][cc] = d + 1
                    q.append((rr, cc, d + 1))

        





