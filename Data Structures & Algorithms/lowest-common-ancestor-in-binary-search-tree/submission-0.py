# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, p, q):
        if root is None:
            return None
        if root==p or root==q:
            return root
        left=self.solve(root.left, p, q)
        right=self.solve(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root                
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.solve(root, p, q)