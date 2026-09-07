from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # goal: return the min num of minutes it will take to rot all oranges 
        # add all the sources to the q
        # r = 2, m = 4
        # [(0,0)(2,2)]
        # [[2,1,1],
        #  [1,1,1]
        # ,[0,1,2]]
        fruit, rotten = 0, 0
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] != 0:
                    fruit += 1
        minutes = 0         
          

        # access a source inc minutes and visit neighbors
        while q:
            is_rotting = False
            
            for i in range(len(q)):
                r, c = q.popleft()
                adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
                rotten += 1
                
                for rr, cc in adj:
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        q.append((rr,cc))
                        grid[rr][cc] = 2
                        is_rotting = True

            if is_rotting:
                minutes += 1
                
        return minutes if rotten == fruit else -1 
