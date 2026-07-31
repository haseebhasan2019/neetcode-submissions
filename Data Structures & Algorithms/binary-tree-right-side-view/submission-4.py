# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque() # [node, level]
        q.append([root, 0])
        res = []
        while q:
            node, level = q.popleft()
            if node:
                if res and level == res[-1][1]:
                    res[-1][0] = node
                else:
                    res.append([node, level])
                q.append([node.left, level+1])
                q.append([node.right, level+1])

        return [node.val for node, _ in res]

# bfs - maintain a node for each level
# update the node for each level as long as level matches