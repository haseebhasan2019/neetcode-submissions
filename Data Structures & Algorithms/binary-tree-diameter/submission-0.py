# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_diameter(node): # returns curr_diam
            if not node:
                return 0
            left_nodes = max_diameter(node.left)
            right_nodes = max_diameter(node.right)
            diameter = left_nodes + right_nodes
            nonlocal max_diam
            max_diam = max(max_diam, diameter)
            return max(left_nodes, right_nodes) + 1

        max_diam = 0
        max_diameter(root)
        return max_diam

#   1
# 2.  3
#    4 6
#   5   7
#  9     8


#   1
# 2.  3
# l=2

#      4 
#   1.   5
# 2.  3.   6
#       5    7
#              8
#                9

#      4 
#   1.    5
# 2.  3.    6
#       5   
#     4   7    
#   5       8
#             9    
# Want to know EACH node's left and right subtree heights and compare that against a max var