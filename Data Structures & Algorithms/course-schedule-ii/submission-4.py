class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        path = []
        finished = 0
        queue = deque([])
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        while queue:
            node = queue.popleft()
            finished += 1
            path.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if numCourses == finished:
            return path
        return []



