class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(row, col, grid):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            way = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in way:
                dfs(row + dr, col + dc, grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, grid)
        return count
        
        