# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque() # queue [(node, level), ...]
        q.append((root, 1))
        rightmost_nodes = [] # stack [val, ...]
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if len(rightmost_nodes) == level:
                rightmost_nodes.pop()
            rightmost_nodes.append(node.val)
            q.append((node.left, level+1))
            q.append((node.right, level+1))
        return rightmost_nodes

# Handle each height level by level
# Breadth first search
# when adding nodes to the queue, tag their level as well
# (node, level)
# the rightmost node will always be the last node per level
# add that node to the list