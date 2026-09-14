from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # goal: return all the cells from which water can flow to both pacific and atlantic
        # multisource bfs
        # p = [4,2,7,3,4,7,6]
        # a = [4,7,6,3,5,3,6]
     

        result = []
        pacific = set()
        atlantic = set()


        rows = len(heights)
        cols = len(heights[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                    
                if r == rows - 1 or c == cols - 1:
                    atlantic.add((r, c))
                
                q.append((r, c))

        while q:
            r, c = q.popleft()
            adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]

            for rr, cc in adj:
                if 0 <= rr < rows and 0 <= cc < cols and heights[rr][cc] >= heights[r][c]:
                
                    if (r, c) in pacific and (rr, cc) not in pacific:
                        pacific.add((rr, cc))
                        q.append((rr, cc))
                    if (r, c) in atlantic and (rr, cc) not in atlantic:
                        atlantic.add((rr, cc))
                        q.append((rr, cc))

                    

        return [[r, c] for r, c in (pacific & atlantic)]

        return result

