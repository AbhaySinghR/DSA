# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def cnt(node):

            if node is None:
                return 0
            
            l=cnt(node.left)
            r=cnt(node.right)
            return 1+l+r
        
        return cnt(root) 
        