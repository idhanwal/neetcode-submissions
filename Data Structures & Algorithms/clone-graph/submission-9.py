"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = set()
        oldToNew = {}
        def dfs(node):
            if node in visit:
                return oldToNew[node]
            visit.add(node)
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                oldToNew[node].neighbors.append(dfs(nei))
        
            return oldToNew[node]
        
        
        return dfs(node)

