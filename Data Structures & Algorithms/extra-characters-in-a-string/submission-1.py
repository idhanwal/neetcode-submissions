class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        root = Trie()

        def addWord(word):
            curr = root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = Trie()
                curr = curr.children[w]
            curr.isWord = True
        
        for word in dictionary:
            addWord(word)
        memo = {}
        def dfs(i, root):
            curr = root
            if i >= len(s):
                return 0
            if i not in memo:
                
                res = 1 + dfs(i + 1, curr)
                for j in range(i, len(s)):
                    if s[j] not in curr.children:
                        break
                    curr = curr.children[s[j]]
                    if curr.isWord:
                        res = min(res, dfs(j + 1, root))
                memo[i] = res
            return memo[i]
        return dfs(0, root)
