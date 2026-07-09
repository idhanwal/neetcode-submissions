class PrefixTree:

    def __init__(self):
        self.path = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch in curr.path:
                curr = curr.path[ch]
            else:
                curr.path[ch] = PrefixTree()
                curr = curr.path[ch]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch in curr.path:
                curr = curr.path[ch]
            else:
                return False
        if curr.isWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch in curr.path:
                curr = curr.path[ch]
            else:
                return False
        return True
        
        