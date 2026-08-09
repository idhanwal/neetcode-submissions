class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            if row[0] <= target <=row[-1]:
                l = 0
                r = n - 1
                while l <= r:
                    m = (l + r) // 2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        return False