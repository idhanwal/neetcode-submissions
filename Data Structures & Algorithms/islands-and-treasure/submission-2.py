class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        queue = deque([])
        m = len(grid)
        n = len(grid[0])
        queue.extend([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dr, dc in directions:
                    x = i + dr
                    y = j + dc

                    if 0 <= x <= m -1 and 0 <= y <= n - 1 and grid[x][y] == INF:
                        queue.append((x, y))
                        grid[x][y] = dist
            dist += 1
