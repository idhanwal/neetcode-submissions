class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            timeSofar, x, y = heapq.heappop(heap)
            if (x, y) in visit:
                continue
            visit.add((x, y))
            if (x, y) == (n - 1, m - 1):
                return timeSofar
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and (nx,  ny) not in visit:
                    time = max(timeSofar, grid[nx][ny])
                    heapq.heappush(heap, (time, nx, ny))
        
            



