class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow():
            for i in range(len(board)):
                nums = set()
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in nums:
                        print("false in rows")
                        return False
                    nums.add(board[i][j])
            return True
        
        def checkCol():
            n = len(board)
            for j in range(n):
                nums = set()
                for i in range(n):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in nums:
                        print("false in col")
                        return False
                    nums.add(board[i][j])
            return True
        
        def checkBlock():
            n = len(board)
            m = 3
            for i in range(3):
                for j in range(3):
                    if not checkMiniblock(i * 3, i * 3 + 3, j * 3, j * 3 + 3):
                        print("false in block")
                        return False
            return True
        
        def checkMiniblock(i1, i2, j1, j2):
            nums = set()
            for i in range(i1, i2):
                for j in range(j1, j2):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in nums:
                        print("false in mini block", i1, i2, j1, j2)
                        return False
                    nums.add(board[i][j])
            return True


        
        return checkRow() and checkCol() and checkBlock()

                    
            