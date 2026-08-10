class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        memo = {}
        def rec(i, j):
            if i >= m or j >= n or (i, j) in visit:
                return float('inf')
            if (i, j) == (m - 1, n - 1) :
                return grid[m - 1][n - 1]
            
            visit.add((i, j))

            if (i, j) not in memo:
                memo[(i, j)] = grid[i][j] + min(rec(i + 1, j), rec(i, j + 1))
                visit.remove((i, j))
            return memo[(i, j)]
        
        return rec(0, 0)