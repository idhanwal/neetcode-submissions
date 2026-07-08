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
        
        old_to_new = {}
        old_to_new[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nie in curr.neighbors:
                if nie not in old_to_new:
                    old_to_new[nie] = Node(nie.val)
                    queue.append(nie)
                old_to_new[curr].neighbors.append(old_to_new[nie])
        return old_to_new[node]

        