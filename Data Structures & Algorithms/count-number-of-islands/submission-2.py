from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find islands and return how many -> it is one or more ones connected 
        # adjacent to each other and surrounded by 0s
        # if we find 0, we skip
        # if we find 1:
            # it may have all neighbors being 0s -> count as one island
            # it may have at least one neighbor being a 1 -> we trace all neighbors 
            # and until we hit the end and count as one island
        # using bfs
        # when we look at element, we mark as seen
        # how do we connect them as one island if adj? -> maintain count until 
            # we get to point where we've seen neighbors, or neighbors are 0s or edges
            # this is when the queue becomes empty
            # continue to next iteration to start new island
         # seen {(0,1),(0,2),(0,3),(1,1),(2,1),(1,3),(2,0)}
        # q = []
        # (3,)
        q = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)] 
        row = len(grid)
        col = len(grid[0])
        seen = set()
        count = 0
        for i in range(row):
            for j in range(col):
                if (i,j) in seen or grid[i][j] == "0":
                    continue
                seen.add((i,j))
                q.append((i,j))
                while q:
                    r, c = q.popleft()
                    seen.add((r,c))
                    # explore all directions of that node
                    for x, y in directions:
                        # if node is a one and not in seen and not out of bounds
                        nx, ny = (r + x), (c + y)
                        if (nx, ny) not in seen:
                            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == "1" :
                                q.append((nx, ny))
                count += 1
        return count
