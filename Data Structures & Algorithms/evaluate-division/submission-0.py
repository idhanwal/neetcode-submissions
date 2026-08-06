class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        graph = defaultdict(list)

        for (n1, n2), w in zip(equations, values):
            graph[n1].append((n2, w))
            graph[n2].append((n1, 1 / w))
        
        
        def bfs(node, target):
            queue = deque([(node, 1)])
            visit = set()
            while queue:
                n, total = queue.popleft()
                if n == target:
                    return total
                for nei, val in graph[n]:
                    if nei not in visit:
                        visit.add(nei)
                        queue.append((nei, total * val))
            return float(-1)
        res = []
        for node, target in queries:
            if node in graph and target in graph:
                res.append(bfs(node, target))
            else:
                res.append(float(-1))
        return res

