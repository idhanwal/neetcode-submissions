# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_invert(root):
            if not root:
                return
            dummy = root.left
            root.left = root.right
            root.right = dummy
            inorder_invert(root.left)
            inorder_invert(root.right)
        
        inorder_invert(root)
        return root
        