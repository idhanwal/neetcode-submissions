# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root, local):
            if not root:
                return
            
            if root.val >= local:
                self.count += 1
                local = root.val
            dfs(root.left, local)
            dfs(root.right, local)
        dfs(root, float('-inf'))
        return self.count
