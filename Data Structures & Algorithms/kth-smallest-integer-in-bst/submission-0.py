# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, store):
            if not root:
                return
            if root.left:
                inOrder(root.left, store)
                # store.append(root.left.val)
            store.append(root.val)
            if root.right:
                inOrder(root.right, store)
                # store.append(root.right.val)
        
        elements = []

        inOrder(root, elements)
        return elements[k - 1]

        