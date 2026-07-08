class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {}
        for n in range(numCourses):
            G[n] = []
        
        for a, b in prerequisites:
            G[a].append(b)
        res = []
        path = set()
        cycle = set()
        
        def dfs(n):
            if n in cycle:
                return False
            if n in path:
                return True
            cycle.add(n)

            for nei in G[n]:
                if dfs(nei) == False:
                    return False
            cycle.remove(n)
            path.add(n)
            res.append(n)
            return True

        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return res