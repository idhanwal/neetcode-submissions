class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        # indegree = [0] * numCourses
        for pre, crs in prerequisites:
            graph[pre].append(crs)
            # indegree[crs] += 1
        ans = []
        for pre, crs in queries:
            queue = deque([pre])
            visit = set()
            visit.add(pre)
            while queue:
                node = queue.pop()
                if node == crs:
                    ans.append(True)
                    break
                for nei in graph[node]:
                    if nei not in visit:
                        queue.append(nei)
                        visit.add(nei)
            else:
                ans.append(False)
        return ans

        

