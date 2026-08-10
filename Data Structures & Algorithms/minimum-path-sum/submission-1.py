class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        m = len(grid)
        n = len(grid[0])
        visit = set()
        while heap:
            dist, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return dist
            if (x, y) in visit:
                continue
            visit.add((x, y))
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit:
                    heapq.heappush(heap, (dist + grid[nx][ny], nx, ny))
            