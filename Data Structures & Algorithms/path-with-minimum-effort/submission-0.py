class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        heap = [(0, 0, 0)]
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            mad, x, y = heapq.heappop(heap)
            if (x, y) in visit:
                continue
            visit.add((x, y))
            if (x, y) == (rows - 1, cols - 1):
                return mad

            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visit:
                    maxAD = max(mad, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(heap, (maxAD, nx, ny))
        return 0
