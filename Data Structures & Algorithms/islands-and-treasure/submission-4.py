class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        queue = deque([])
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
        
        dist = 1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != -1 and (ni, nj) not in visit:
                        visit.add((ni, nj))
                        grid[ni][nj] = min(grid[ni][nj], dist)
                        queue.append((ni, nj))
            dist += 1
        

