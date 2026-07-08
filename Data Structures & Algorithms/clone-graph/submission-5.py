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

        new = {}
        new[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.pop()
            for nei in cur.neighbors:
                if nei not in new:
                    new[nei] = Node(nei.val)
                    queue.append(nei)
                new[cur].neighbors.append(new[nei])
        
        return new[node]
        