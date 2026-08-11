"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        def dfs(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]
            oldToNew[node] = Node(node.val)
            oldToNew[node].next = dfs(node.next)
            oldToNew[node].random = dfs(node.random)
            return oldToNew[node]
        
        return dfs(head)


