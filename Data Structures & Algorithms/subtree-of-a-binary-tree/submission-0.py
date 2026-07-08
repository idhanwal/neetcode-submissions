# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subtree):
            if not root and subtree:
                return False
            
            if isSameTree(root, subtree):
                return True
            
            return dfs(root.left, subtree) or dfs(root.right, subtree)
        
        def isSameTree(root1, root2):
            if root1 and root2:
                if root1.val == root2.val:
                    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
                else:
                    return False
            elif not root1 and not root2:
                return True    
            return False
        
        return dfs(root, subRoot)

        