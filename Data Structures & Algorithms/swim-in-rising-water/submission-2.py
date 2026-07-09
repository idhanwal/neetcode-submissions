class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = 0
        visit = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            st, x, y = heapq.heappop(heap)
            t = max(t, st)
            if (x, y) == (m -1, n - 1):
                return t

            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
        
        return t

