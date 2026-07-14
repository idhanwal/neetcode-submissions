class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # G = {i : [] for i in range(n)}
        # for node, nei in edges:
        #     G[node].append(nei)
        #     G[nei].append(node)
        
        # cycle = set()

        # def dfs(n, prev):
        #     if n in cycle:
        #         return False

        #     cycle.add(n)

        #     for nei in G[n]:
        #         if nei == prev:
        #             continue
        #         if not dfs(nei, n):
        #             return False
            
        #     return True

        # if not dfs(0, -1):
        #     return False
        
        # for i in range(n):
        #     if i not in cycle:
        #         return False
        # return True

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
            size[px] += size[py]
            parent[py] = px
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        return self.components == 1






