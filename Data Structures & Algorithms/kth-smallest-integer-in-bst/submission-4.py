# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        count = 0
        def inOrder(root):
            if root:
                nonlocal res, count
                inOrder(root.left)
                count+=1
                if count == k:
                    res = root.val
                    return
                inOrder(root.right)
        inOrder(root)
        return res