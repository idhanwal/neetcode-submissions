class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = max(t, time)

            for nei, t2 in graph[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (time + t2, nei))
        
        return t if len(visit) == n else -1