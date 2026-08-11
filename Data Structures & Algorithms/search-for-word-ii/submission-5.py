class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Trie()

        for word in words:
            root.addWord(word)
        
        m = len(board)
        n = len(board[0])
        res = set()

        def dfs(i, j, root, word, visit):
            if min(i, j) < 0 or i >= m or j >= n or (i, j) in visit or board[i][j] not in root.children:
                return
            visit.add((i, j))
            word += board[i][j]
            root = root.children[board[i][j]]
            if root.isWord:
                res.add(word)
            
            dfs(i + 1, j, root, word, visit)
            dfs(i - 1, j, root, word, visit)
            dfs(i, j + 1, root, word, visit)
            dfs(i, j - 1, root, word, visit) 
            visit.remove((i, j))


        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    visit = set()
                    dfs(i, j, root, "", visit)
        return list(res)



        
            



