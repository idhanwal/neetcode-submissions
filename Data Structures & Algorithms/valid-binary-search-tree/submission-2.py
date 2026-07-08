# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check_bst(root, min, max):
            if not root:
                return True
            
            if root.val > min and root.val < max:
                return True and (check_bst(root.left, min, root.val) and check_bst(root.right, root.val, max))
            return False
        return check_bst(root, -1001, 1001)