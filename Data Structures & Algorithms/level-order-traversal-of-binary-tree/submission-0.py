# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((0,root))
        res = []
        while q:
            level, node = q.popleft()
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.append((level+1,node.left))
            if node.right:
                q.append((level+1,node.right))
        return res

# maintain a queue of the TreeNodes that need to be explored
# (level, TreeNode)
# Add to the res list based on the level itself