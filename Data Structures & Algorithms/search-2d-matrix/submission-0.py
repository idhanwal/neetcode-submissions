class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:
            l = 0
            r = len(row) - 1

            while l <= r:
                m = (r + l) // 2 
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False 
