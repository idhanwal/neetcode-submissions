class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isWord = True
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""

        trie = Trie()

        for word in strs:
            trie.addWord(word)
        curr = trie
        while len(curr.children.keys()) == 1 and not curr.isWord:
            key = list(curr.children.keys())[0]
            res += key
            curr = curr.children[key]
        return res

