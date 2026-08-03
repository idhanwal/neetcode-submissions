# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val < val:
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(val)
                    break
        return root