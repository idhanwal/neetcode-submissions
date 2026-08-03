# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndex = 0
        def build_tree(inorder):
            if self.preorderIndex >= len(preorder):
                return None
            
            if inorder:
                root = TreeNode(preorder[self.preorderIndex])
                self.preorderIndex += 1
                inorderIndex = inorder.index(root.val)
                root.left = build_tree(inorder[:inorderIndex])
                root.right = build_tree(inorder[inorderIndex + 1:])
                return root
            return None
        
        return build_tree(inorder)
