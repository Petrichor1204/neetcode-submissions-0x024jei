from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # goal: return the num of minutes to rot the fruits
        # [[[2,1,1],
        #   [1,1,1],
        #   [0,1,2]]
        #  q = [(0,0), (2,2)] [(2,1), (1,2)] [(1,1)] [(0,1)] [(0,0)]
        # fresh = 1
        time = 0
        fresh = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #ewns

        # add all the sources
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1


        # explore the paths of all the sources
        while q:
            length = len(q)
            rotted = False
            for i in range(length):
                r, c = q.popleft()
                for x, y in directions:
                    nr, nc = x + r, y + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotted = True
                        q.append((nr, nc))
            
            # increment time if rot happened
            if rotted:
                time += 1
                

        return time if fresh == 0 else -1
        

        # return time
