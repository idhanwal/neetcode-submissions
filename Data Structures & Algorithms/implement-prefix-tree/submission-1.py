class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = Trie()
                curr = curr.children[ch]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        if curr.isWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return True
        
        