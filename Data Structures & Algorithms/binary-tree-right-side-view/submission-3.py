# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque() # [node, level]
        q.append([root, 0])
        res = []
        res.append([root,0])
        while q:
            node, level = q.popleft()
            if level == res[-1][1]:
                res[-1][0] = node
            else:
                res.append([node, level])
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])

        return [node.val for node, _ in res]

# bfs - maintain a node for each level
# update the node for each level as long as level matches