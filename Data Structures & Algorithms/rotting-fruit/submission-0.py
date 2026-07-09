class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dr, dc in directions:
                    nr, nc = i + dr, j + dc

                    if 0 <= nr <= m - 1 and 0 <= nc <= n - 1 and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1
        

        
