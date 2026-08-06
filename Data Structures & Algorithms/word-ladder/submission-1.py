class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        variations = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                variation = word[:i] + "*" + word[i + 1:]
                variations[variation].append(word)

        queue = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        transformations = 0
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                print(word)
                if word == endWord:
                    return transformations + 1
                for i in range(len(word)):
                    variation = word[:i] + "*" + word[i + 1:]
                    for option in variations[variation]:
                        if option not in visit:
                            visit.add(option)
                            queue.append(option)
            transformations += 1
        
        return 0