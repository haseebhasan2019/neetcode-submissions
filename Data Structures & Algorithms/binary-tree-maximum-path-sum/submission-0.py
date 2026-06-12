# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        val = node.val
        self.res = max(self.res, val, val+l, val+r, val+l+r)
        return max(val, val+l, val+r)
