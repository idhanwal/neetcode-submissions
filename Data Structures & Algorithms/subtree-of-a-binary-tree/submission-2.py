# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def traverse(p, q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val != q.val:
                return False

            return True and (traverse(p.left, q.left) and traverse(p.right, q.right))
        
        queue =[]
        queue.append(root)
        same = None
        while queue:
            node = queue.pop()
            if node.val == subRoot.val and traverse(node, subRoot):
                return True
            if node and node.left:
                queue.append(node.left)
            elif node and node.right:
                queue.append(node.right)
        return False