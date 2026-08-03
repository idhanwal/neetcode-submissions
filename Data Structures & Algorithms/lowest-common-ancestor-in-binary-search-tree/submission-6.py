# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.lca = None
        def dfs(root, p, q):
            if not root:
                return
            
            if root.val < p.val and root.val < q.val:
                dfs(root.right, p, q)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left, p, q)
            else:
                self.lca = root
        
        dfs(root, p, q)
        return self.lca