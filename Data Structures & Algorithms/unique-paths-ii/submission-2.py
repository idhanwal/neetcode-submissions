class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        # memo = {}
        # visit = set()
        # def rec(i, j):
        #     if i >= m or j >= n or (i, j) in visit or obstacleGrid[i][j] == 1:
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
        grid[m - 1][n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    grid[i][j] += grid[i + 1][j] + grid[i][j + 1]
                else:
                    grid[i][j] = 0
        
        return grid[0][0]