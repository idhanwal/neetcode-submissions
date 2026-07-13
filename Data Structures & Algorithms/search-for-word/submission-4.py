class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, idx, visit):
            if idx == len(word):
                return True
            if min(i, j) < 0 or i >= m or j >= n or (i, j) in visit or board[i][j] != word[idx]:
                return False
            # idx += 1
            visit.add((i, j))

            res = (dfs(i + 1, j, idx + 1, visit) 
            or dfs(i - 1, j, idx + 1, visit)
            or dfs(i, j + 1, idx + 1, visit)
            or dfs(i, j - 1, idx + 1, visit))
            visit.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                if board[i][j] == word[0] and dfs(i, j, 0, visit):
                    return True
        return False