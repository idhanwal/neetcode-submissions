class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        # indegree = [0] * (numCourses)

        for a, b in prerequisites:
            graph[a].append(b)
            # indegree[b] += 1
        
        # queue = deque([])
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)
        # coursesCompleted = 0
        # while queue:
        #     node = queue.popleft()
        #     coursesCompleted += 1
        #     for nei in graph[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             queue.append(nei)
        # return True if coursesCompleted == numCourses else False
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if graph[crs] == []:
                return True
            visiting.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            graph[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        