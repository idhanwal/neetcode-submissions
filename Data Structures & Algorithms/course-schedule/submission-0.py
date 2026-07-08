class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()

        def dfs(n):
            if n in visited:
                return False
            
            if graph[n] == []:
                return True
            
            visited.add(n)
            for pre in graph[n]:
                if not dfs(pre):
                    return False
            visited.remove(n)
            graph[n] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True