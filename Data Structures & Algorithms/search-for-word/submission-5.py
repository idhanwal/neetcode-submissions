class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def dfs(i, j, visit, index):
            if index >= len(word):
                return True
            if min(i, j) < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visit or board[i][j] != word[index]:
                return False
            visit.add((i, j))
            res = False
            for di, dj in directions:
                res = res or dfs(i + di, j + dj, visit, index + 1)
            
            visit.remove((i, j))
            return res
        answer = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, set(), 0):
                    return True
        return False
                    
                    
            

            

