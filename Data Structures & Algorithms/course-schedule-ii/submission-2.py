class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            G[crs].append(pre)
        

        visit, cycle = set(), set()

        path = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in G[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            path.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return path
        