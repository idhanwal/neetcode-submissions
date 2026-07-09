class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        """

        variants = defaultdict(list)

        for word in wordList:
            for i in range(0, len(word)):
                variant = word[:i] + "*" + word[i + 1:]
                variants[variant].append(word)
        
        queue = deque([beginWord])

        steps = 0
        seen = set()
        seen.add(beginWord)
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps + 1
                for i in range(len(word)):
                    variant = word[:i] + "*" + word[i + 1:]
                    for option in variants[variant]:
                        if option not in seen:
                            seen.add(option)
                            queue.append(option)
            steps += 1
        return 0


