class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # goal: return true if a word is found in the board else false
        # dfs + backtracking
        # board=[["a"]]
        # word="a"
        rows = len(board)
        cols = len(board[0])
        visited = set()
        is_found = False

        def word_search(r, c, i, curr_word):
            nonlocal is_found
            curr_word.append(board[r][c])

            # termination - word found
            if "".join(curr_word) == word:
                is_found = True
                return

            # base case - if letter not target
            if board[r][c] != word[i]:
                return
                
            visited.add((r, c))

            # continuation - explore neighbors
            adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in adj:
                if (dr, dc) not in visited and 0 <= dr < rows and 0 <= dc < cols:
                    word_search(dr, dc, i + 1, curr_word)
                    curr_word.pop()
                    
            visited.remove((r, c))
                    

        # looking for the start letter
        for r in range(rows):
            for c in range(cols):
                word_search(r, c, 0, [])
        
        return is_found