# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find_good_nodes(node, curr_max):
            if not node:
                return 0
            if node.val < curr_max:
                return find_good_nodes(node.left, curr_max) + find_good_nodes(node.right, curr_max)
            else:
                return 1 + find_good_nodes(node.left, node.val) + find_good_nodes(node.right, node.val)
    
        return find_good_nodes(root, float("-inf"))