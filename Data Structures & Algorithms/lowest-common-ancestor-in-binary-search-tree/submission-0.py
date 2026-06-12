# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        while res != None:
            if res.val < p.val and res.val < q.val:
                res = res.right
            elif res.val > p.val and res.val > q.val:
                res = res.left
            else:
                return res
# Get the Path
# p: 5 3
# q: 5 8 
# res = common = 5

# p: 5 3 4
# q: 5 3
# res = common = 5 3