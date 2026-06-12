# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=0
        count=0

        def inOrder(node):
            if node:
                nonlocal count
                inOrder(node.left)
                count += 1
                if count == k:
                    nonlocal res 
                    res = node.val
                    return
                inOrder(node.right)
        inOrder(root)
        return res
    

# perform an in-order traversal of the binary tree
# keep a count of nodes in the traversal
# once the count reaches size k, return that node