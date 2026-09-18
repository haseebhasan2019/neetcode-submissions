# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                l.append(node.val)
        traverse(root)
        return l

# 4, 5, 2, 6, 7, 3, 1