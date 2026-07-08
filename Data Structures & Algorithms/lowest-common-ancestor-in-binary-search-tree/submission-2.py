# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        queue = [root]

        while queue:
            node = queue.pop()

            if node.val > p.val and node.val > q.val:
                queue.append(node.left)
            elif node.val < p.val and node.val < q.val:
                queue.append(node.right)
            # elif (p.val <= node.val and q.val >= node.val) or (q.val <= node.val and p.val >= node.val):
            else:
                return node
        