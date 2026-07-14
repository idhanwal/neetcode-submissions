class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(0, n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
        ans = []
        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
               ans = [x, y]
        
        return ans