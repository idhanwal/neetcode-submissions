# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_height(root):
            if not root:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)

            if left > right:
                return 1 + left
            return 1 + right
        return get_height(root)