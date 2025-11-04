# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        self.s=0

        def lsum(node):

            if not node:
                return 0
            
            if node.left and node.left.left==None and node.left.right==None:
                self.s+=node.left.val
            
            lsum(node.left)
            lsum(node.right)
        
        lsum(root)

        return self.s
        