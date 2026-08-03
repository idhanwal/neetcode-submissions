"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def isSame(self, grid):
        n = len(grid)
        value = grid[0][0]
        row = [value] * n
        for r in grid:
            if r != row:
                return (False, False)
        return (True, True if value else False)

    def construct(self, grid: List[List[int]]) -> 'Node':
        isLeaf, value = self.isSame(grid)
        if isLeaf:
            root = Node(value, isLeaf, None, None, None, None)
            return root
        root = Node(value)
        root.isLeaf = False
        n = len(grid)
        half = n // 2
        root.topLeft = self.construct([row[: half] for row in grid[:half]])
        root.topRight = self.construct([row[half:] for row in grid[: half]])
        root.bottomLeft = self.construct([row[: half] for row in grid[half:]])
        root.bottomRight = self.construct([row[half:] for row in grid[half:]])
        return root


