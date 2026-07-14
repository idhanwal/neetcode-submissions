class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)
        self.components = n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            self.components -= 1
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
            return True
        
        for a,b in edges:
            union(a, b)
        print(size)
        return self.components
                

        