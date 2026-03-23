# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValue(r):
            curr = r
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def remove(root,val):
            if not root:
                return None
            
            if val > root.val:
                root.right = remove(root.right,val)
            elif val < root.val:
                root.left = remove(root.left,val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = minValue(root.right)
                    root.val = minNode.val
                    root.right = remove(root.right,minNode.val)
            return root   
        
        return remove(root,key)
