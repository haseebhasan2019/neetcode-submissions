# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = self.inOrder(root, [])
        return l[k-1]

    def inOrder(self, root, res) -> []:
        if not root:
            return res
        res = self.inOrder(root.left, res)
        res.append(root.val)
        res = self.inOrder(root.right, res)
        
        return res
        


# Assemble the list in order then return the kth smallest
# In-order traversal
