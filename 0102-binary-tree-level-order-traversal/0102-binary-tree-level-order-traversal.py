# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        level = []
        l = 0
        queue = deque([(root,0)])

        while queue:
            node, nodelevel = queue.popleft()

            if not node:
                continue
            
            if nodelevel != l:
                levels.append(level[:])
                level = []
                l += 1
            
            level.append(node.val)
            queue.append((node.left, l + 1))
            queue.append((node.right, l + 1))
        
        if level:
            levels.append(level[:])

        return levels