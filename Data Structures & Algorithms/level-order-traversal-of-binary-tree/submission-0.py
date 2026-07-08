# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_height(root):
            if not root:
                return 0
            
            left = get_height(root.left)
            right = get_height(root.right)
            if left > right:
                return 1 + left
            return 1 + right
        
        def dfs(root, level, current_level, result):
            if not root:
                return
            
            if current_level == level:
                result.append(root.val)
            elif current_level < level:
                dfs(root.left, level, current_level + 1, result)
                dfs(root.right, level, current_level + 1, result)
        if not root:
            return []
        height = get_height(root)
        print(height)
        res = [[] for _ in range(height)]
        print(res)
        for h in range(1, height + 1):
            dfs(root, h, 1, res[h-1])
        
        return res