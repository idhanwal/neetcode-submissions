# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_valid_bst(root, maximum, minimum):
            if not root:
                return True
            if root.val > minimum and root.val < maximum:
                return check_valid_bst(root.left, root.val, minimum) and check_valid_bst(root.right, maximum, root.val)
            return False
        
        return check_valid_bst(root, 1001, -1001)