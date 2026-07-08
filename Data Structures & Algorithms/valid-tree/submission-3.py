class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        G = {i : [] for i in range(n)}
        for node, nei in edges:
            G[node].append(nei)
            G[nei].append(node)
        
        cycle = set()

        def dfs(n, prev):
            if n in cycle:
                return False

            cycle.add(n)

            for nei in G[n]:
                if nei == prev:
                    continue
                if not dfs(nei, n):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        
        for i in range(n):
            if i not in cycle:
                return False
        return True
        