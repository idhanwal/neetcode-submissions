class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        path = []
        completed = 0
        while queue:
            node = queue.popleft()
            path.append(node)
            completed += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if completed == numCourses:
            return path
        return []

        


        

