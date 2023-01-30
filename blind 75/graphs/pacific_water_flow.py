class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def are_valid_coord(r, c):
            return 0 <= r < ROWS and 0<= c < COLS

        def get_neighbours(r, c):
            return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        def dfs(r, c, prevHeight, visited):
            if not are_valid_coord(r, c):
                return
                
            curr_height = heights[r][c]
            if (r, c) in visited or \
                    curr_height < prevHeight:
                return

            visited.add((r, c))
            for r_neighbour, c_neighbour in get_neighbours(r, c):
                dfs(r_neighbour, c_neighbour, curr_height, visited)

        for c in range(COLS):
            dfs(0, c, 0, pac)
            dfs(ROWS -1, c, 0, atl)

        for r in range(ROWS):
            dfs(r, 0, 0, pac)
            dfs(r, COLS - 1, 0, atl)

        res = []
        for item in pac:
            if item in atl:
                res.append(item)
        return res

print(Solution().pacificAtlantic([[3,3,3],[3,1,3],[0,2,4]]))