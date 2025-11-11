# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:


        self.fmin=float('inf')
        self.prev=None
        def mindiff(node):
            if not node:
                return
            mindiff(node.left)
            if self.prev is not None:
                self.fmin = min(self.fmin, abs(node.val - self.prev))
            self.prev = node.val
            mindiff(node.right)
        
        mindiff(root)
        return self.fmin
        

            
        