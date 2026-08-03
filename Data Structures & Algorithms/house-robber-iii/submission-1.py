# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(root, robbed):
            if (root, robbed) in memo:
                return memo[(root, robbed)]
            if not root:
                # self.res = max(amount, self.res)
                return 0
            memo[(root, robbed)] = 0
            if robbed:
                memo[(root, robbed)] = dfs(root.left, 0) + dfs(root.right, 0)
            else:
                pick = root.val + dfs(root.left, 1) + dfs(root.right, 1)
                notPick = dfs(root.left, 0) + dfs(root.right, 0)
                memo[(root, robbed)] = max(pick, notPick) 
            return memo[(root, robbed)]
        
        return dfs(root, 0)
            
