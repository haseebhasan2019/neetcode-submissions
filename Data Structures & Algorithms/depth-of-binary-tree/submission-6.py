# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_height(node, height):
            if not node:
                return height
            return max(get_height(node.left, height+1), get_height(node.right, height+1))

        return get_height(root, 0)