class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def neigbours(cell):
            r, c = cell
            return [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]

        def not_valid(cell):
            r, c = cell
            return not (0 <= r < ROWS and 0 <= c < COLS)
        
        def dfs(cell, i=0):
            r, c = cell
            if not_valid(cell) or board[r][c]!=word[i]:
                return False
            # print(board[r][c], cell, i)
            if len(word)-1==i: return True

            board[r][c] = ' '
            res = any(dfs(neighbour, i+1) for neighbour in neigbours(cell))

            board[r][c] = word[i]
            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = (r, c)
                if dfs(cell, i=0): return True
        
        return False
