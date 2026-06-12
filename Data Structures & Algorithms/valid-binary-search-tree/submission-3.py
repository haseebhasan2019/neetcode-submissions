# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -1001, 1001)

    def validate(self, root, minimum, maximum):
        if not root:
            return True
        if root.left and (root.left.val < minimum or root.left.val > (root.val-1)):
            return False
        if root.right and (root.right.val < root.val+1 or root.right.val > maximum):
            return False
        return self.validate(root.left, minimum, root.val-1) and self.validate(root.right, root.val+1, maximum)