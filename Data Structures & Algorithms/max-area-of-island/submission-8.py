class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = find(x)
        py = find(y)

        if px == py:
            return False
        if size[px] < size[py]:
            px, py = py, px
        parent[py] = px
        size[px] += size[py]
        return True

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        def dfs(i, j):
            if min(i, j) < 0 or i >= rows or j >= cols or (i, j) in visit or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            visit.add((i, j))
            res = 0
            for dr, dc in directions:
                res += dfs(i + dr, j + dc)
            
            return 1 + res
        
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans

        