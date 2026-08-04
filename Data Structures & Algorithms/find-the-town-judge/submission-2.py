class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in trust:
            graph[a].append(b)
            # graph[b].append(a)
        print(graph)
        count = 0
        res = 0
        for i in range(1, n + 1):
            if i not in graph:
                for key in graph:
                    if i not in graph[key]:
                        break
                else:
                    count += 1
                    res = i
        return res if count == 1 else -1
