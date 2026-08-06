class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        

        heap = [(0, k)]
        visit = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return time
            for nei, w in graph[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + w, nei))
        return -1

            