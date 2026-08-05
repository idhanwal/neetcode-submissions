class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)


        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
