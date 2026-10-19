# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.are_matching(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def are_matching(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            return self.are_matching(root.left, subRoot.left) and self.are_matching(root.right, subRoot.right)
        else:
            return False
'''
traverse through all the nodes the nodes in root's tree
if a node matches the subroot root, then call are_matching_trees which iterates through them together until subroot or root completes
'''