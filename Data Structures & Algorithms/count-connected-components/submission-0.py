class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = {i: [] for i in range(n)}
        for node, nei in edges:
            G[node].append(nei)
            G[nei].append(node)
        
        visit = set()

        def dfs(n):
            if n in visit:
                return
            
            visit.add(n)

            for nei in G[n]:
                # if nei == parent:
                #     continue
                dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count


            

        