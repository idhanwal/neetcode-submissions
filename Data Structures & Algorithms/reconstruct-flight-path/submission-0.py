class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for a, b in tickets[::-1]:
            graph[a].append(b)
        
        res = []
        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs("JFK")
        return res[::-1]
            


