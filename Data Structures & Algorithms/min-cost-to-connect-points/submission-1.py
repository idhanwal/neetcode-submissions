class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = []

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    md = abs(xi - xj) + abs(yi - yj)
                    graph.append((md, i, j))
        
        graph.sort()

        parent = [i for i in range(len(points))]
        size = [1] * len(points)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if size[px] < size[py]:
                px, py = py, px
            size[px] += size[py]
            parent[py] = px
            return True
        res= 0
        for dist, u, v in graph:
            if union(u, v):
                res += dist
        return res
