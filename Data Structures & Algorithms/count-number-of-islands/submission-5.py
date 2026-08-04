class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        def dfs(i, j):
            if min(i, j) < 0 or i >= rows or j >= cols or (i, j) in visit or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            visit.add((i, j))
            for dr, dc in directions:
                dfs(i + dr, j + dc)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

