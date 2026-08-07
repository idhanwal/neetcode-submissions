class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for word in words for c in word}
        indegree = {key : 0 for key in graph}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([])
        for key in graph:
            if indegree[key] == 0:
                queue.append(key)
        
        path = []
        while queue:
            node = queue.popleft()
            path.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(path) != len(indegree):
            return ""
        return "".join(path)




