class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r: int, c: int) -> bool:
            s = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in s:
                        return False
                    s.add(val)
            return (grid[r][c] + grid[r][c + 1] + grid[r][c + 2] == 
                    grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] == 
                    grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] ==
                    grid[r][c] + grid[r + 1][c] + grid[r + 2][c] ==
                    grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] ==
                    grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] ==
                    grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] ==
                    grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c])
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r + 1][c + 1] == 5 and is_magic(r, c):
                    count += 1
        
        return count
