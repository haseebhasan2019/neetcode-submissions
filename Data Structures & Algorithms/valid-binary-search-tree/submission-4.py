# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minimum, maximum):
            if not node:
                return True
            if minimum < node.val < maximum:
                return isValid(node.left, minimum, node.val) and isValid(node.right, node.val, maximum)
            return False
        return isValid(root, float('-inf'), float('inf'))
# Each node is bound by (minimum, maximum)
#   left -> (minimum, node.val)
#   right-> (node.val, maximum)