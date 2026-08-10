class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # visit = set()
        # def rec(i, j):
        #     if i >= m or j >= n or (i, j) in visit:
        #         return 0
        #     if (i, j) == (m - 1, n - 1):
        #         return 1
        #     visit.add((i, j))
        #     if (i, j) not in memo:
        #         memo[(i, j)] = rec(i + 1, j) + rec(i, j + 1)
        #         visit.remove((i, j))
            
        #     return memo[(i, j)]
        
        # return rec(0, 0)

        grid = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        
        return grid[m - 1][n - 1]
