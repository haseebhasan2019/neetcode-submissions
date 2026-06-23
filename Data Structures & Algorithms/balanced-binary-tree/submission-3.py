# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.get_height(root.left) - self.get_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        return max(left, right) + 1

# For each node, get the left and right height and compare