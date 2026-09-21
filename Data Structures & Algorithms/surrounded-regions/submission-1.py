from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # goal: turn surrounded regions' zeros to xs
        # first: find the surrounded regions
        # second: turn x's to zeros
        ["O","X","X","O","X"],
        ["X","O","O","X","O"],
        ["X","O","X","O","X"],
        ["O","X","O","O","O"],
        ["X","X","O","X","O"]

        rows = len(board)
        cols = len(board[0])
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        q.append((r, c))
                        

        while q:
            r, c = q.popleft()
            visited.add((r, c))
            adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]

            for rr, cc in adj:
                if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == "O" and (rr, cc) not in visited:
                    q.append((rr, cc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] == "O":
                    visited.add((r, c))
                    board[r][c] = "X"



        






