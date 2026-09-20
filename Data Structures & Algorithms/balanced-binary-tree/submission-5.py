# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_depth(node):
            if not node:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            return 1 + max(left, right)
        
        if not root:
            return True
        left = get_depth(root.left)
        right = get_depth(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

# We need to get the depth from each node
# We need to bubble up true or false depending on whether each subtree is valid or not