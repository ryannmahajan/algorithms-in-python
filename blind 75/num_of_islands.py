class Solution:
    def new_island(self, grid, r, c, island_mark):
        island_mark+=1
        grid[r][c] = island_mark
        print(f"Creating island {island_mark} at {r},{c}")
        return island_mark

    def numIslands(self, grid: list[list[str]]) -> int:
            
        total_rows = len(grid)
        total_cols = len(grid[0])
        
        island_mark = 1
        
        for r in range(total_rows):
            for c in range(total_cols):
                print(f"at r={r}, c={c}, {grid[r][c]}")
                if grid[r][c]=='0':
                    continue
                    
                if c==0 and r==0:
                    island_mark = self.new_island(grid, r, c, island_mark)
                    continue
                    
                get_from_c, get_from_r = c-1, r
                if c==0:
                    get_from_c, get_from_r = 0, r-1
                
                if grid[get_from_r][get_from_c]=='0':
                    island_mark = self.new_island(grid, r, c, island_mark)                    
                else: grid[r][c] = grid[get_from_r][get_from_c]
        
        return island_mark - 1
                    
a= [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

Solution().numIslands(a)