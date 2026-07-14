class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visit = set()
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 1

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for r, c in directions:
                    nx, ny = x + r, y + c
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visit and grid[nx][ny] != -1:
                        visit.add((nx, ny))
                        grid[nx][ny] = min(grid[nx][ny], dist)
                        queue.append((nx, ny))
            dist += 1
        
