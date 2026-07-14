class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque([])
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        finished = 0
        while queue:
            node = queue.popleft()
            finished += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return numCourses == finished
