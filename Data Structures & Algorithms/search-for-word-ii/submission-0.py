class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ans = []
        for word in words:
            trie.addWord(word)
        
        def dfs(i, j, root, word, visit):
            if min(i, j) < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visit or board[i][j] not in root.children:
                return 
            ch = board[i][j]
            visit.add((i, j))
            word += ch
            node = root.children[ch]
            if node.isWord:
                ans.append(word)
                node.isWord = False

            dfs(i + 1, j, root.children[ch], word, visit) 
            dfs(i - 1, j , root.children[ch], word, visit)
            dfs(i, j + 1, root.children[ch], word, visit)
            dfs(i, j - 1, root.children[ch], word, visit)
            
            visit.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                if board[i][j] in trie.children:
                    dfs(i, j, trie, "", visit)
        
        return ans


            

        