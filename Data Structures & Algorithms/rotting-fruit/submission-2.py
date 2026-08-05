class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque([])
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    visit.add((i, j))
                    queue.append((i, j))
        

        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while fresh and queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visit and grid[ni][nj] == 1:
                        fresh -= 1
                        visit.add((ni, nj))
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
            time += 1
        
        return time if fresh == 0 else -1

